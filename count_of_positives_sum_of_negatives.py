"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


"""

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    positives = sum([1 for i in arr if i > 0])
    negatives = sum([i for i in arr if i < 0])
    return [positives, negatives]
  
  # another example
  
  def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []
