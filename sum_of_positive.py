# sum of positive

# you get an array of numbers, return the sum of all of the positive ones.
# example [1,-4,7,12] => 1 + 7 + 12 = 20
# note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
  return sum(i for i in arr if i > 0)

# another method

def positive_sum(arr):
  sum = 0
  for i in arr:
    if i > 0:
      sum += e
  return sum

# another method

def positive_sum(arr):
  return sum(filter(lambda x: x > 0, arr))
