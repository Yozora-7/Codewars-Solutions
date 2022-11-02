"""

"""

def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False
      
# another example

def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)
