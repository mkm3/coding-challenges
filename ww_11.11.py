# def maxofthree(num1, num2, num3):
#     """Returns the largest of three integers
    
#     >>> maxofthree(1, 5, 2)
#     5

#     >>> maxofthree(10, 1, 11)
#     11
#     """

#     # return max(num1,num2,num3)

# #max = none
#     max = None
# #if num1 > num2 = max
#     if num1 > num2:
#         max = num1
#     else:
#         max = num2
# #if max > num3 = return max  ----> runtime 0(1)
#     if max > num3:
#         return max
#     else:
#         return num3

#iterating through the parameters
    #they comparing the num the other num

#sorting algorithm
    #after sort, take last indix


#using max method

#calculator
#elements = stack


# print(maxofthree([1,2,3], [1,2,5], [1,2,4])) #max() works if data_structure is the same
# print(maxofthree([1,2,3], [1,2,5], [1,3,4]))
# print(maxofthree(10, 1, 11))

def calc(s):
    """Evaluate expression."""

    # calc("* 2 + 1 2")
    # [['*', 2], ['+', '1', '2']]

    # operations = #list of lists

    running_sum = 0

    # pancake = list(reversed(s.split(' ')))
    
    operations = s

    while operations:
        #list = pop list at end
        pancake = operations.pop()
        
        for i in range(1, len(pancake)):
            num = int(pancake[i])
            operator = pancake[0]
            if operator == '-':
                running_sum -= num
            elif operator == '+':
                running_sum += num
            elif operator == '/':
                running_sum = running_sum / num
            elif operator == '*':
                running_sum = running_sum * num
    
    return running_sum

    # elements = list(reversed(s.split(' ')))
    # return(elements)

print(calc([['*', '2'], ['+', '1', '2']]))

#     if '-':
#         a = a[0] - a[2]

#     elif '+':
#         a = a[0] - a[2]

#     elif '/':
#         a = a[0] / a[2]

#     else:
#         a = a[0] * a[2]


#To-do - figure out how to create multiple lists for our stacks
