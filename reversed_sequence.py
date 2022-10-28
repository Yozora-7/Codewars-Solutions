"""
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
"""

def reverse_seq(n):
    i = list(range(n, 0, -1))
    return i
  
# another example

reverse_seq = lambda n: list(range(n, 0, -1))

# another example

def reverse_seq(n):
    return [x for x in range(1,n+1)][::-1]
