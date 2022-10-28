# sum without highest and lowest number

# sum all the numbers of a given array (cq.list), except the highest and the lowest element (by value,
# not by index!)

# the highest or lowest element respectively is a single element at each edge, even if there are more
# than one with the same value.

def sum_array(arr):
  return 0 if arr == None or len(arr) < 3 else sum(arr) - min(arr) - max(arr))

# another example

def sum_array(arr):
  if arr == None or len(arr) < 3:
    return 0
  return sum(arr) - max(arr) - min(arr)

