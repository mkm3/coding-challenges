#recursive solution
def rev_list_in_place(lst):
  """Reverse list in place. You cannot do this with 
  reversed(), .reverse(), or list slice assignment!
  """

  #helper function - using recursion
  def helper(left,right):
    #if index/left is less that index/right
    if left < right:
      #left,right value is now right,left
      lst[left], lst[right] = lst[right], lst[left]
      #calling helper to move left pos to the right one and right pos to the left one
      #iteration by recursion
      helper(left + 1, right - 1)
  #function calling passing starting index pos and ending pos
  helper(0, len(lst) - 1)

  return lst


#non-recursive solution
def rev_list_in_place2(lst):
  """Reverse list in place. You cannot do this with 
  reversed(), .reverse(), or list slice assignment!
  """

  i = 0

  while i < len(lst) / 2:
    #current pos, last index of the list - current pos = last index of the list - current pos, current pos
    lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    i += 1
  return lst


  # #helper function - using recursion
  # def helper(left,right):
  #   #if index/left is less that index/right
  #   if left < right:
  #     #left,right value is now right,left
  #     lst[left], lst[right] = lst[right], lst[left]
  #     #calling helper to move left pos to the right one and right pos to the left one
  #     #iteration by recursion
  #     helper(left + 1, right - 1)
  # #function calling passing starting index pos and ending pos
  # helper(0, len(lst) - 1)

  # return lst

print(rev_list_in_place([3, 2, 1]))
print(rev_list_in_place2([3, 2, 1]))

