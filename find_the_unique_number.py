"""

"""

def find_uniq(arr):
    arr.sort()
    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]
    return n 
  
# another example

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
