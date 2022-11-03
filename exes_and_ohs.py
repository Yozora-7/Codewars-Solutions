"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):

    o = s.lower().count('o')
    x = s.lower().count('x')

    if o == x : return True
    elif o != x : return False
    else:
        return True
      
# another example

def xo(s):
    return s.lower().count('x') == s.lower().count('o')
