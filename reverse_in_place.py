def rev_list_in_place(lst):
  """Reverse list in place.

  You cannot do this with reversed(), .reverse(), or list slice
  assignment!
  """

  #helper function - using recursion
  def helper(left,right):
    if left < right:
      lst[left], lst[right] = lst[right], lst[left]
      helper(left + 1, right - 1)

  helper(0, len(lst)-1)

  return lst

print(rev_list_in_place([3, 2, 1]))