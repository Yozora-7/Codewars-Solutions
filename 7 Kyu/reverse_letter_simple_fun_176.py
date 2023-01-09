"""

"""

import re

def reverse_letter(string):
    num = r'[0-9\W_]' # numbers from 0-9, \ means to escape a special character, the W matches any non-word character except _, so we put the _.
    return re.sub(num, "", string[::-1]) # return a substring with replaced values. We are replacing any character found in num with "". 
  
# another example

def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1] # is alphanumerical.
