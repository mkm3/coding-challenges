# def has_balanced_parens(phrase):
#   """Does a string have balanced parentheses?"""

#   paren_dict = {
#     ")" : 0,
#     "(" : 0
#     }

#   for char in phrase:
#     if char == ")":
#       paren_dict[")"] += 1
#     if char == "(":
#       paren_dict["("] += 1
  
#   if paren_dict["("] == paren_dict[")"]:
#     print("True")
#     return True
#   else:
#     print("False")
#     return False

#   print(paren_dict["("])
#   print(paren_dict[")"])
#   print("\n", paren_dict)



# def has_balanced_parens(phrase):
#   """Does a string have balanced parentheses?"""

  # paren_dict = {
  #   ")" : 0,
  #   "(" : 0
  #   }
  # left_paren_ct = 0
  # right_paren_ct = 0

  # for char in phrase:
  #   if char == ")":
  #     right_paren_ct += 1
  #   if char == "(":
  #     left_paren_ct += 1
  
  # if left_paren_ct == right_paren_ct:
  #   print("True")
  #   return True
  # else:
  #   print("False")
  #   return False

  # return left_paren_ct == right_paren_ct

  # print(left_paren_ct)
  # print(right_paren_ct)
  # print("\n", (left_paren_ct, right_paren_ct))

def has_balanced_parens(phrase):
  paren_ctr = 0
  for char in phrase:
    if char == "(":
      paren_ctr += 1
    elif char == ")":
      paren_ctr -= 1
    
    if paren_ctr < 0:
      return False

  return paren_ctr == 0


print(has_balanced_parens("()")) #True
print(has_balanced_parens(")(")) #False
print(has_balanced_parens("(Oh Noes!)(")) #False
has_balanced_parens("((There's a bonus open paren here.)") #False
has_balanced_parens(")") #False
has_balanced_parens("(") #False
has_balanced_parens("(This has (too many closes.) ) )") #False

