def is_palindrome(word):
  """Return True/False if this word is a palindrome."""

  i = 0

  while i < len(word) / 2:
    if word[i] == word[len(word) - 1 - i]:
      i += 1
    else: 
      return False
  return True


print(is_palindrome("a")) #True
print(is_palindrome("noon")) #True
print(is_palindrome("racecar")) #True
print(is_palindrome("porcupine") )#False