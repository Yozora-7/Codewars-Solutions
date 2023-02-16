"""
Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""

def encrypt_this(text):
    words = text.split(" ")
    res = []
    for i in words:
        new = ""
        temp = ""
        for j in range(len(i)):
          if j == 0:
            new += str(ord(i[j]))
          elif j == 1:
            temp = i[j]
            new += i[-1]
          elif j == len(i) - 1:
            new += temp
          else:
            new += i[j]  
        res.append(new)
    return " ".join(list(filter(None, res))) 
  
# another example

def swapper(w):
    return w if len(w)<2 else w[-1] + w[1:-1] + w[0]

def encrypt_this(s):
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in s.split())
