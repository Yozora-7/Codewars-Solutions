# sum without highest and lowest number

def sum_array(arr):
  return 0 if arr == None or len(arr) < 3 else sum(arr) - min(arr) - max(arr))

# another example

def sum_array(arr):
  if arr == None or len(arr) < 3:
    return 0
  return sum(arr) - max(arr) - min(arr)

