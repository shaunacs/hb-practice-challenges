"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""

# Itierate through the string
# Keep track of current char
# Count each repeating char
# Varibale that holds compressed version of string


def compress(string):
    """Return a compressed version of the given string."""

    compressed = ""
    current_char = string[0]    # a
    char_count = 0
    idx = 0
                    #2
    while idx < (len(string) - 1):
            # a             # a
        if string[idx] != current_char:
            char_count = 0
            current_char = string[idx]
            idx += 1
        else:
            if char_count == 0:
                compressed = f'{compressed}{string[idx]}'
                current_char = string[idx]
                idx += 1
            else:
                compressed = f'{compressed}{string[idx]}{char_count}'
                char_count = 0
                current_char = string[idx]
                idx += 1


    # for char in string:
    #     if char == current_char:
    #         char_count += 1
    #         current_char = 
    #     else:
    #         if char_count == 0:
    #             compressed = f'{compressed}{char}'
    #         else:
    #             compressed = f'{compressed}{char}{char_count}'
    #             char_count = 0
    
    return compressed



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
