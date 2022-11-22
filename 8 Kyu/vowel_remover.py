"""
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
don't worry about uppercase vowels
y is not considered a vowel for this kata
"""

def shortcut(s):
    vowels = 'aeiou'
    for i in s:
        if i in vowels:
            s = s.replace(i, "")
    return s
  
# another example

def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')
