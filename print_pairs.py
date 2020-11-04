"""
Practice Question 2: Part One

Given an array of unique positive integers and a target value, 
print all pairs of integers from the array whose sum is equal 
to the target

Example:
numbers = [3, 10, 2, 6, 8, 5],
target = 8 solution = (3,5) (2,6)

"""

def print_pairs(arr, target):

    #empty list to hold pairs
    pairs = []

    #n is length of array
    n = len(arr)

    #keeps track of index from range 0-n
    for i in range(0, n):
        #keeps track of another index from range i + 1, n
        for j in range(i + 1, n):
            #condition to evaluate if two elements = target
            if ((arr[i] + arr[j]) == target):
                #if so, append to our pairs list
                pairs.append((arr[i], arr[j]))
    return pairs

print("\n Part 1")
print(print_pairs([3, 10, 2, 6, 8, 5], 8)) #(3,5) (2,6)


"""
Part 2 - pairs should not repeat themselves
"""

def print_pairs(arr, target):

    # #to remove duplicates, speed runtime
    # arr = set(arr)
    # arr = list(arr)

    #empty set to hold pairs
    pairs = set()

    #n is length of array
    n = len(arr)

    #keeps track of one element
    for i in range(0, n):
        #keeps track of another element
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == target):
                pairs.sorted(set((arr[i], arr[j])))
    # arr.pop(0)
    return pairs

print("\n Part 2")
print(print_pairs([3, 10, 2, 6, 8, 3, 2, 6, 5], 8))
print(print_pairs([3, 2, 5, 6, 3, 5, 3 ], 8)) #not able to get this edge case #solution #(3,5) (2,6), (3, 5)
print(print_pairs([1, 1, 2, 2, 2], 3)) #not able to get this edge case #solution = (1,2) (1,2)

