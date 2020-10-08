import math
import os
import random
import re
import sys


def jumpingOnClouds(c):

    counter = 0
    i = 0
    while i < len(c) - 1:

        if i < len(c) - 2 and c[i + 2] == 0:
            i += 2
        else:
            i += 1

        counter += 1
    return counter

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])) #4
print(jumpingOnClouds([0, 0, 0, 0, 1, 0])) #3
print(jumpingOnClouds([0, 0, 0, 1, 0, 0])) #3

