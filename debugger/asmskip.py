# SPDX-FileCopyrightText: 2025 Jarmo Tiitto <jarmo.tiitto@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later
"""Accurate skipping past and out of conditional code blocks."""
import dis
from collections import namedtuple

# pylint disable=R1710, R0915

_asmskip_opcode_cache = {}

def disassemble(f_code):
    '''Disassemble a code object, with jump info.
       * Instruction columns are resolved to a minimum column of the originating source line.
         'RESUME' instruction is ignored for the code object's minimum column.
       * Any instructions part of an source line that does a jump are marked as "jumping".
       * Returns a AsmInstr list and the code object's minimum column.
    '''
    # A simple associative cache.
    entry = _asmskip_opcode_cache.get(f_code, None)
    if entry:
        return entry
    # Later ins part of a lineno can change already appended AsmInstr(s):
    # A proxy list objects are used to allow updating the past AsmInstr(s).
    AsmInstr = namedtuple(
        'AsmInstr', [
            'opcode',
            'opname',
            'oparg',
            'lineno',
            'offset',
            'jump_target',
            'column',
            'jumping'
        ])
    asm_list = []
    lineno_info = {}
    min_column = -1
    for ins in dis.get_instructions(f_code):
        lineno = -1 if ins.line_number is None else ins.line_number
        column = -1 if ins.positions.col_offset is None else ins.positions.col_offset
        if ins.opcode != dis.opmap['RESUME']:
            if min_column == -1:
                min_column = column
            min_column = min(min_column, column)
        if lineno not in lineno_info:
            lineno_info[lineno] = [[column], [False]]
        if lineno_info[lineno][0][0] > column:
            lineno_info[lineno][0][0] = column
        if ins.jump_target is not None:
            lineno_info[lineno][1][0] = True
        asm_list.append(AsmInstr(
            ins.opcode,
            ins.opname,
            ins.argrepr,
            lineno,
            ins.offset,
            ins.jump_target,
            lineno_info[lineno][0],
            lineno_info[lineno][1]))
    asm_list = [AsmInstr(x[0], x[1], x[2], x[3], x[4], x[5], x[6][0], x[7][0]) for x in asm_list]
    _asmskip_opcode_cache[f_code] = (asm_list, min_column)
    return asm_list, min_column


_asmskip_stepout_cache = {}

def stepout_lineno(f_code, curr_lineno):
    '''Look ahead in the code object and find a source line past curr_line such that:
       1. Skip past a single block if it starts at the curr_lineno source line.
       2. Step out from "for", "while" and "if" blocks:
          Blocks contained in the curr_lineno source line's block and after it line are skipped.
       3. Else, return -1.
    '''
    jump_targets = {} # set of the forward jump instr offsets
    forend_lineno = -1
    ins = None # current AsmInstr (updated in the for-loop)
    # The code is arranged into inner functions.
    process_goal = None
    def past_endfor():
        if forend_lineno < ins.lineno:
            return ins.lineno
        return None

    def maybe_reached_jump_target():
        if ins.opcode != dis.opmap['END_FOR']:
            return ins.lineno
        # Find next ins with greater than ins.lineno:
        nonlocal forend_lineno
        forend_lineno = ins.lineno
        nonlocal process_goal
        process_goal = past_endfor
        return None

    # Jump target updating.
    jump_filter = None

    def want_all_jumps():
        if ins.jump_target is not None and ins.jump_target > ins.offset:
            nonlocal jump_targets
            jump_targets[ins.jump_target] = False

    def want_no_jumps():
        return

    def want_next_jump():
        if ins.jump_target is not None and ins.jump_target > ins.offset:
            nonlocal jump_targets
            # discard all earlier jump targets, only ins.jump_target is wanted.
            jump_targets.clear()
            jump_targets[ins.jump_target] = False
            nonlocal jump_filter
            jump_filter = want_no_jumps

    def past_single_jump():
        nonlocal process_goal
        nonlocal jump_targets
        nonlocal jump_filter
        if jump_targets.pop(ins.offset, False):
            jump_filter = want_no_jumps
            ret = maybe_reached_jump_target()
            if ret is not None:
                return ret
        return None

    # seek_to_curr_lineno() requires min_column
    asm_list, min_column = disassemble(f_code)

    def seek_to_curr_lineno():
        '''find first ins of curr_lineno source line.'''
        nonlocal jump_targets
        if ins.lineno < curr_lineno:
            # Discard reached jump targets while seeking to first ins of curr_lineno.
            jump_targets.pop(ins.offset, None)
            return None
        # Reached first ins of curr_lineno.
        # ins can be a target of earlier jump. We want to go past it, so discard it.
        jump_targets.pop(ins.offset, None)
        nonlocal process_goal
        nonlocal jump_filter
        if ins.jumping:
            # Find a target past of this starting single block.
            process_goal = past_single_jump
            # Accept the soon following jump target.
            jump_filter = want_next_jump
            return None
        if ins.column <= min_column or not jump_targets:
            # No pending jump targets exist, or the starting ins.column is <= min_column.
            return -1
        # Find a target past of the current block.
        # New jump targets are ignored.
        process_goal = past_single_jump
        jump_filter = want_no_jumps
        return None

    # get cached starting index.
    cache = _asmskip_stepout_cache.setdefault(id(f_code), {})
    if curr_lineno in cache:
        index = cache[curr_lineno]
    else:
        # (binary search would be nice, except asm_list is not sorted by lineno.)
        index = 0
        for index, ins in enumerate(asm_list):
            if ins.lineno >= curr_lineno:
                break
        until_index = index
        while index > 0:
            if asm_list[index].column <= min_column:
                break
            index -= 1
        for i in range(index, until_index):
            cache[asm_list[i].lineno] = index

    # Process loop.
    process_goal = seek_to_curr_lineno
    jump_filter = want_all_jumps
    for ins in asm_list[index:]:
        # track forward jump targets.
        jump_filter()
        if ins.offset in jump_targets:
            jump_targets[ins.offset] = True
        ret = process_goal()
        if ret is not None:
            return ret
    return -1
