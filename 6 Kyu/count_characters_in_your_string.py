"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(string):
    my_dict = {}
    for i in string:
        my_dict[i] = my_dict.get(i, 0) + 1 # the dict 'a' will be equal to 1 every time it is found
    return my_dict
  
  # another example
  
from collections import Counter

def count(string):
    return Counter(string)
