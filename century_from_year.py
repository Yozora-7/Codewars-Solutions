"""
Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.
"""

def century(year):
    return (year - 1) //  100 + 1 # tp calculate the century would be to divide the year by 100 + 1  for odd numbers (floor division)

# another example

import math

def century(year):
    return math.ceil(year / 100)
