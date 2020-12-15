def has_balanced_parens(phrase):
  """Does a string have balanced parentheses?"""

  paren_dict = {
    ")" : 0,
    "(" : 0
    }

  for char in phrase:
    if char == ")":
      paren_dict[")"] += 1
    if char == "(":
      paren_dict["("] += 1
  
  if paren_dict["("] == paren_dict[")"]:
    print("True")
    return True
  else:
    print("False")
    return False

  print(paren_dict["("])
  print(paren_dict[")"])
  print("\n", paren_dict)


has_balanced_parens("()") #True
has_balanced_parens("(Oh Noes!)(") #False
has_balanced_parens("((There's a bonus open paren here.)") #False
has_balanced_parens(")") #False
has_balanced_parens("(") #False
has_balanced_parens("(This has (too many closes.) ) )") #False