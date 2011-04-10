import sys

def processpy(arg):
    filename = arg[11:].strip()
    try:
        with open(filename, 'rb') as py:
            code = py.readlines()
    except IOError as e:
        print('Could not process %s: %r' % (filename, e))
        return arg
    lines = []
    for number, line in enumerate(code):
        if '"' in line:
            print('Warning double quote found in line %d' % number)
        lines.append('"' + line.strip('\n').replace('"', "'") + r'\n"')
    
    return '\n'.join(lines) + '\n' + arg

for arg in sys.argv[1:]:
    print('Opening %s' % arg)
    try:
        with open(arg, 'rb') as src:
            with open(arg[:-3], 'wb') as dst:
                for line in src:
                    if line.startswith(';// python:'):
                        dst.write(processpy(line))
                    else:
                        dst.write(line)
        print('Output writen to %s' % arg[:-3])                    
    except IOError as e:
        print('Could not process %s: %r' % (filename, e))
