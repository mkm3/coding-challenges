import math
import os
import random
import re
import sys


def hourglassSum(arr):

    # final = ldk

    results = []
    #identify what makes the hourglass/shape 
    top = arr[0][0] + arr[0][1] + arr[0][2]
    middle = arr[1][1]
    bottom = arr[2][0] + arr[2][1] + arr[2][2] 

    hourglass = top + middle + bottom
    #rows = 6
    #cols = 6

    # stop two before end, so that we don't break the list
    for row in range(len(arr) - 2):
        for col in range(len(arr) - 2):
            results.append(hourglass +)
        
        #move through 
        # for num in lst:


if __name__ == '__main__':

    print(hourglassSum([[-9, -9, -9,  1, 1, 1], --1
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]]))


""" Michelle C's
def hourglassSum(arr):
    max_hg = arr[0][0] + arr[0][1] + arr[0][2]\
           + arr[1][1]\
           + arr[2][0] + arr[2][1] + arr[2][2]
    
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            current_hg = top + middle + bottom 
            max_hg = max(max_hg, current_hg) # updating max_hg to be either current hourglass or the max_hg
    
    return max_hg
"""
""" Michelle C's Jumping clouds
def jumpingOnClouds(c):

    count = 0
    idx = 0

    # iterate through array of ints until reach end 
    while idx < len(c) - 1:
        # if current cloud is 0, then increment index an extra 1
        # accounts for if jumping forward 2 spaces
        if c[idx] == 0:
            idx += 1
        # increase counter and idx each iteration
        count += 1
        idx += 1

    print(count)
    return count
"""

"""
Michelle M.
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

"""

""" SARAH"S 
def jumpingOnClouds(c):
    jumps = 0
    idx = 0
    last = n-1
    while idx < last:
        # if you can jump two, jump two
        if (idx + 2 <= last) and (c[idx+2] == 0):
            idx += 2
            jumps += 1
        # jump one
        elif c[idx+1] == 0:
            idx += 1
            jumps += 1
        
    return(jumps)
"""

"""SARAH's
    def hourglassSum(arr):
    build_hourglass = []
    for i in range(0,4):
        for j in range(0, 4):
            build_hourglass.append(sum([arr[i][j]+arr[i][j+1], arr[i][j+2], \
                                         arr [i+1][j+1], \
                                        arr [i+2][j], arr[i+2][j+1], arr[i+2][j+2]]))
    
    return(max(build_hourglass))
"""

""" LARENA
def hourglassSum(arr):
    result = []
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            if i < 4 and j < 4:
                sumation = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i +2][j] + arr[i + 2][j + 1] + arr[i +2][j + 2]
                result.append(sumation)
    result.sort()
    return result[-1]
"""

