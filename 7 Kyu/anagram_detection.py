"""
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"
"""

def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
  
# another example

def is_anagram(test, original):
    test_dict, original_dict = {}, {}
    for i in test.lower():
        test_dict[i] = test_dict.get(i, 0) + 1
    for i in original.lower():
        original_dict[i] = original_dict.get(i, 0) + 1
        
    return test_dict == original_dict
