"""
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.
"""

def no_odds(values):
    return [value for value in values if value % 2 == 0]
  
# another example

def no_odds(values):
    list = []
    for i in values:
        if i % 2 == 0:
            list.append(i)
    return list
