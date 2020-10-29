"""
Practice Question 1
Given two strings, determine if one string is a permutation of the other.

Example:
Input 1: “cd”, “dc”
Output 1: true

Input 2: “aab”, “aba”
Output 2: true

Input 3: “zzyy”, “yzzz”
Output 3: false
"""

#func to iterate through string1
def iterate(string):

    char_list = []

    for char in string:
        char_list.append(char)
    
    return char_list
            

def is_anagram(s1, s2):

    #check if length of s1 = s2
    #if not same length

    if len(s1) != len(s2):
        return False

    #if characters in s1 == s2
    else:
        s1 = iterate(s1)
        s2 = iterate(s2)

        if s1 == s2:
            return True
        else:
            return False

print(is_anagram("zzyy", "yzzz")) #False
print(is_anagram("aab", "aba")) #True
