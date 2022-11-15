"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    return ''.join(list(map(upper, list(s))))
    
def upper(letter):
    return ' ' + letter if letter.isupper() else letter
