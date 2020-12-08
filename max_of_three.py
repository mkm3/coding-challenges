def maxofthree_v1(num1, num2, num3):
    """Returns the largest of three integers
    
    >>> maxofthree(1, 5, 2)
    5

    >>> maxofthree(10, 1, 11)
    11
    """

    return max(num1,num2,num3)

print(maxofthree_v1(1, 5, 2))
print(maxofthree_v1(10, 1, 11))


def maxofthree_v2(num1, num2, num3):
    """Returns the largest of three integers
    
    >>> maxofthree(1, 5, 2)
    5

    >>> maxofthree(10, 1, 11)
    11
    """

    max_num = 0

    if num1 >= num2:
        max_num = num1

    else:
        max_num = num2

    if num2 >= num3:
        max_num = num2

    else:
        max_num = num3

    return max_num

print(maxofthree_v2(1, 5, 2))
print(maxofthree_v2(10, 1, 11))

