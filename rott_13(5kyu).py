"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

def rot13(message):
    lst = []
    for letter in message:
        lst.append(newLetter(letter))
    return "".join(lst)
        
def newLetter(letter):
    if str(letter).isdigit():
        return letter
    
    if 65 <= ord(letter) <= 90: # ord returns the letter's ascii value. If the value is between 65 and 90,
        new_letter = ord(letter) + 13 # then it will create a new value equal to the current number + 13.
        return chr(new_letter) if new_letter <= 90 else chr(64 + new_letter % 90) # convert the new variable back from an ascii value to a digit.
    
    elif 97 <= ord(letter) <= 122: # check for lowercase now
        new_letter = ord(letter) + 13
        return chr(new_letter) if new_letter <= 122 else chr(96 + new_letter % 122)   
    
    return letter # cater to special characters, which should just be returned.
  
  # another example
  
  import string

def rot13(message):
    return ''.join(chr((65 if c.isupper() else 97) + ((ord(c) - (65 if c.isupper() else 97)) + 13)%26) if c.isalpha() else c for c in message)
    
