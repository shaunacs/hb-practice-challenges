"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""

#Grab last character
# append it to a variable

def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """

    if astring != "":
        chars = []
        for char in astring:
            chars.append(char)
        while chars:
            return f'{chars.pop(-1)}{rev_string("".join(chars))}'



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. !KROW DOOG\n")
