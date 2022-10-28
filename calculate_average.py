# write a function which calculates the average of the numbers in a given list.

# note: empty arrays should return 0.

def find_average(numbers):
   return sum(numbers) / len(numbers)
  
  # another example
  
  def find_average(array):
    if len(array) != 0:
      return sum(array) / len(array)
    else:
      return 0
    
    
