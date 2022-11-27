"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""

def duplicate_encode(word):
    word = word.lower()
    st = ""
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1 # get the first char and set it to 1 every time it is found
    for i in word:
        if dict[i] > 1:
            st += ")"
        else:
            st +="("
    return st
  
# another example

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
