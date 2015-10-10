class RegexObject():
    """
   The :class:`RegexObject` class supports the following methods and attributes:
        """

    def search(self, string, pos, endpos):
        """

        Scan through *string* looking for a location where this regular expression
        produces a match, and return a corresponding :class:`MatchObject` instance.
        Return ``None`` if no position in the string matches the pattern; note that this
        is different from finding a zero-length match at some point in the string.

        The optional second parameter *pos* gives an index in the string where the
        search is to start; it defaults to ``0``.  This is not completely equivalent to
        slicing the string; the ``'^'`` pattern character matches at the real beginning
        of the string and at positions just after a newline, but not necessarily at the
        index where the search is to start.

        The optional parameter *endpos* limits how far the string will be searched; it
        will be as if the string is *endpos* characters long, so only the characters
        from *pos* to ``endpos - 1`` will be searched for a match.  If *endpos* is less
        than *pos*, no match will be found, otherwise, if *rx* is a compiled regular
        expression object, ``rx.search(self, string, 0, 50)`` is equivalent to
        ``rx.search(self, string[:50], 0)``.

        >>> pattern = re.compile(self, "d")
        >>> pattern.search(self, "dog")     # Match at index 0
        <_sre.SRE_Match object at ...>
        >>> pattern.search(self, "dog", 1)  # No match; search doesn't include the "d"


    """
        return MatchObject()
    def match(self, string, pos, endpos):
        """

        If zero or more characters at the *beginning* of *string* match this regular
        expression, return a corresponding :class:`MatchObject` instance.  Return
        ``None`` if the string does not match the pattern; note that this is different
        from a zero-length match.

        The optional *pos* and *endpos* parameters have the same meaning as for the
        :meth:`~search` method.

        >>> pattern = re.compile(self, "o")
        >>> pattern.match(self, "dog")      # No match as "o" is not at the start of "dog".
        >>> pattern.match(self, "dog", 1)   # Match as "o" is the 2nd character of "dog".
        <_sre.SRE_Match object at ...>

        If you want to locate a match anywhere in *string*, use
        :meth:`~search` instead (self, see also :ref:`search-vs-match`).


    """
        return MatchObject()
    def split(self, string, maxsplit=0):
        """

        Identical to the :func:`split` function, using the compiled pattern.


    """
        return [str()]
    def findall(self, string, pos, endpos):
        """

        Similar to the :func:`findall` function, using the compiled pattern, but
        also accepts optional *pos* and *endpos* parameters that limit the search
        region like for :meth:`match`.


    """
        return [str()]
    def finditer(self, string, pos, endpos):
        """

        Similar to the :func:`finditer` function, using the compiled pattern, but
        also accepts optional *pos* and *endpos* parameters that limit the search
        region like for :meth:`match`.


    """
        return [str()]
    def sub(self, repl, string, count=0):
        """

        Identical to the :func:`sub` function, using the compiled pattern.


    """
        return str()
    def subn(self, repl, string, count=0):
        """

        Identical to the :func:`subn` function, using the compiled pattern."""
        return str()

    flags = str()
    groups = int()
    groupindex = {"None": int()}
    pattern = SRE_Pattern()

class MatchObject:
    """
   Match objects always have a boolean value of ``True``.
   Since :meth:`~regex.match` and :meth:`~regex.search` return ``None``
   when there is no match, you can test whether there was a match with a simple
   ``if`` statement::

      match = re.search(self, pattern, string)
      if match:
          process(self, match)
   """
    def expand(self, template):
        """

        Return the string obtained by doing backslash substitution on the template
        string *template*, as done by the :meth:`~sub` method.  Escapes
        such as ``\n`` are converted to the appropriate characters, and numeric
        backreferences (self, ``\1``, ``\2``) and named backreferences (self, ``\g<1>``,
        ``\g<name>``) are replaced by the contents of the corresponding group.


        """
        return str()
    def group(self, group1, *args):
        """

        Returns one or more subgroups of the match.  If there is a single argument, the
        result is a single string; if there are multiple arguments, the result is a
        tuple with one item per argument. Without arguments, *group1* defaults to zero
        (self, the whole match is returned). If a *groupN* argument is zero, the corresponding
        return value is the entire matching string; if it is in the inclusive range
        [1..99], it is the string matching the corresponding parenthesized group.  If a
        group number is negative or larger than the number of groups defined in the
        pattern, an :exc:`IndexError` exception is raised. If a group is contained in a
        part of the pattern that did not match, the corresponding result is ``None``.
        If a group is contained in a part of the pattern that matched multiple times,
        the last match is returned.

            >>> m = re.match(self, r"(self, \w+) (self, \w+)", "Isaac Newton, physicist")
            >>> m.group(self, 0)       # The entire match
            'Isaac Newton'
            >>> m.group(self, 1)       # The first parenthesized subgroup.
            'Isaac'
            >>> m.group(self, 2)       # The second parenthesized subgroup.
            'Newton'
            >>> m.group(self, 1, 2)    # Multiple arguments give us a tuple.
            (self, 'Isaac', 'Newton')

        If the regular expression uses the ``(self, ?P<name>...)`` syntax, the *groupN*
        arguments may also be strings identifying groups by their group name.  If a
        string argument is not used as a group name in the pattern, an :exc:`IndexError`
        exception is raised.

        A moderately complicated example:

            >>> m = re.match(self, r"(self, ?P<first_name>\w+) (self, ?P<last_name>\w+)", "Malcolm Reynolds")
            >>> m.group(self, 'first_name')
            'Malcolm'
            >>> m.group(self, 'last_name')
            'Reynolds'

        Named groups can also be referred to by their index:

            >>> m.group(self, 1)
            'Malcolm'
            >>> m.group(self, 2)
            'Reynolds'

        If a group matches multiple times, only the last match is accessible:

            >>> m = re.match(self, r"(self, ..)+", "a1b2c3")  # Matches 3 times.
            >>> m.group(self, 1)                        # Returns only the last match.
            'c3'


    """
        return str() if False else [str()]
    def groups(self, default):
        """

        Return a tuple containing all the subgroups of the match, from 1 up to however
        many groups are in the pattern.  The *default* argument is used for groups that
        did not participate in the match; it defaults to ``None``.  (self, Incompatibility
        note: in the original Python 1.5 release, if the tuple was one element long, a
        string would be returned instead.  In later versions (self, from 1.5.1 on), a
        singleton tuple is returned in such cases.)

        For example:

            >>> m = re.match(self, r"(self, \d+)\.(self, \d+)", "24.1632")
            >>> m.groups(self, )
            (self, '24', '1632')

        If we make the decimal place and everything after it optional, not all groups
        might participate in the match.  These groups will default to ``None`` unless
        the *default* argument is given:

            >>> m = re.match(self, r"(self, \d+)\.?(self, \d+)?", "24")
            >>> m.groups(self, )      # Second group defaults to None.
            (self, '24', None)
            >>> m.groups(self, '0')   # Now, the second group defaults to '0'.
            (self, '24', '0')


    """
        return [str()]
    def groupdict(self, default):
        """

        Return a dictionary containing all the *named* subgroups of the match, keyed by
        the subgroup name.  The *default* argument is used for groups that did not
        participate in the match; it defaults to ``None``.  For example:

            >>> m = re.match(self, r"(self, ?P<first_name>\w+) (self, ?P<last_name>\w+)", "Malcolm Reynolds")
            >>> m.groupdict(self, )
            {'first_name': 'Malcolm', 'last_name': 'Reynolds'}


    """
        return {"foo": "foo"}
    def start(self, group):
        """
                end(self, [group])

        Return the indices of the start and end of the substring matched by *group*;
        *group* defaults to zero (self, meaning the whole matched substring). Return ``-1`` if
        *group* exists but did not contribute to the match.  For a match object *m*, and
        a group *g* that did contribute to the match, the substring matched by group *g*
        (self, equivalent to ``m.group(self, g)``) is ::

            m.string[m.start(self, g):m.end(self, g)]

        Note that ``m.start(self, group)`` will equal ``m.end(self, group)`` if *group* matched a
        null string.  For example, after ``m = re.search(self, 'b(self, c?)', 'cba')``,
        ``m.start(self, 0)`` is 1, ``m.end(self, 0)`` is 2, ``m.start(self, 1)`` and ``m.end(self, 1)`` are both
        2, and ``m.start(self, 2)`` raises an :exc:`IndexError` exception.

        An example that will remove *remove_this* from email addresses:

            >>> email = "tony@tiremove_thisger.net"
            >>> m = re.search(self, "remove_this", email)
            >>> email[:m.start(self, )] + email[m.end(self, ):]
            'tony@tiger.net'


    """
        return -1
    def span(self, group):
        """

        For :class:`MatchObject` *m*, return the 2-tuple ``(self, m.start(self, group),
        m.end(self, group))``. Note that if *group* did not contribute to the match, this is
        ``(self, -1, -1)``.  *group* defaults to zero, the entire match."""
        return (0, 0)

    pos = 0
    endpos = 0
    lastindex = 0
    lastgroup = "None"
    re = RegexObject()
    string = "None"

SRE_Match = MatchObject
SRE_Pattern = RegexObject