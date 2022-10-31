"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

def grow(arr):
    total = 1
    for i in arr:
        total *= i
    return total
  
  # another example
  
  import math
def grow(arr):
    return math.prod(arr) # the prod method is used to calculate the product of all the elements present in the given iterable.
