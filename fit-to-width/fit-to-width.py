"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

#PSEUDOCODE
# Count to limit
# Track what is contained within that limit
# Check if there is a space
# Print what is before that space
# Make new starting point to be after the space

def fit_to_width(string, limit):
    """Print string within a character limit."""

    all_words = string.split()

    while all_words != []:
        current_line = ""
        for idx, word in enumerate(all_words):
            if (len(current_line) + len(word)) <= limit:
                current_line = current_line + word
                all_words.pop(idx)
            else:
                print(current_line)
                current_line = ""



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
