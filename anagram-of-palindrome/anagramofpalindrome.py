"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""
#PSEUDOCODE
# make an empty dict to hold count of letters
# loop over letters in word
# if letter in dict, += dict[letter]
# else dict[letter] = 1
# empty list of even numbers of letters
# empty list of odd numbers of letters
# loop over dict
# if dict value % 2 == 0:
# append that key to list of even number of letters
# else append to odd number of letters
# if len(odd number of letters) is greater than 1, return False
# else return True

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_count = {}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    even_count = []
    odd_count = []

    for letter in letter_count:
        if letter_count[letter] % 2 == 0:
            even_count.append(letter)
        else:
            odd_count.append(letter)
    
    if len(odd_count) > 1:
        return False
    else:
        return True

    


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
