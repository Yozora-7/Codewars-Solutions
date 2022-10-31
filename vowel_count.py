"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        count += sentence.count(i)
    return count
    
# another example

def getCount(s):
    return sum(c in 'aeiou' for c in s)
