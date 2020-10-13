import math
import os
import random
import re
import sys

def repeatedString(s, n):

    #keep track of number of "a"s
    counter = 0

    #to find out how many complete compies of the string go into "n"
    total_substring = n // len(s)

    #to find out how many characters are remaining for the incomplete substring "n"
    remainder_substring = n % len(s)

    #new_string that is "n" characters long
    new_string = s * total_substring + s[0:remainder_substring]

    for char in new_string:
        if char == "a":
            counter += 1

    return counter

print(repeatedString("abcac", 13))




def repeatedString2(s, n):

    total_substring = n // len(s)
    remaining_substring = n % len(s)

    num_a_in_s = 0
    num_a_in_remainder_s = 0


    for idx, char in enumerate(s):
        if char == "a":
            num_a_in_s += 1
            if idx < remaining_substring:
                num_a_in_remainder_s += 1
                
    return (num_a_in_s * total_substring) + num_a_in_remainder_s

print(repeatedString2("abcac", 13))
