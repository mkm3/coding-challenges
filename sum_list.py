def sum_list(num_list):
  """Return the sum of all numbers in list."""

  total = 0

  for num in num_list:
    total += num
  return total
  
print(sum_list([5, 3, 6, 2, 1]))