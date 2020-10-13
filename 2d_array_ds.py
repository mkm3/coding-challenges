
def sum_hourglasses(arr):
    ""
    # array has to be 6 x 6
    arr = [
    cols for j in columns    |
    j =  0, 1, 2, 3, 4, 5    |
        -------->            V
        [x, x, x, a, 1, 1], --> rows i = 0  --> range(6) --> starting idx 0 --> (6-1)
        [0, x, 0, 0, a, 0], --> rows i = 1
        [x, x, x, a, a, a], --> rows i = 2
        [1, 1, 1, 0, 0, 0], --> rows i = 3
        [$, $, $, 0, 0, 0], --> rows i = 4
        [1, $, 1, 0, 0, 0], --> rows i = 5
    ]
    ""
    top = arr[0][0] + arr[0][1] + arr[0][2]   
    middle = arr[1][11] 
    bottom = arr[2][0] + arr[2][1] + arr[2][2]
    first_hourglass = top + middle + bottom

    # all_hourglasses = [first_hourglass] # --> [-9, -29, -100, -6] 
    max_hourglass = first_hourglass # max() --> must not have an empty array inside
    # max hourglass correct answer --> -6 [-9, -29, -100, -6]

    rows = len(arr)  # [[], [], [], [], [], []]
    cols =  len(arr[0]) # 6 ^ --> [0, 0, 0, 0, 0, 0]
    # matrix / grid --> chess board, square, rectangle --> rows = height, cols = width
    for row in range(len(arr) - 2): # range(6) -> range(0, 6) --> [0, 1, 2, 3, 4, 5]
        for col in range(cols - 2): # [0, 1, 2, 3, 4, 5]
            # moving left or right --> col is moving + 1 or - 1 or +2
            # moving up or down --> row is + 1 or -1 or + 2
            top = arr[row + 0][col + 0] + arr[row + 0][col + 1] + arr[row + 0][col + 2]   
            middle = arr[row + 1][col + 11] 
            bottom = arr[row + 2][col + 0] + arr[row + 2][col + 1] + arr[row + 2][col + 2]

            total_hourglass = top + middle + bottom
            max_hourglass = max(total_hourglass, max_hourglass)
            # all_hourglasses.append(total_hourglass)
    return max_hourglass

            # arr[0][0] == arr[row][col]
            # arr[0][0 + 1] == arr[row][col + 1]

    
    # # runtimes
    # for loop fhsdjkflskdjf ---> O(n)
    # + 
    # for loop skdfjalksdfja ---> O(n)
    # O(n)

    # for fkdsjklafjsdfa 
    #     for dlkjfalksdf
    # # nested --> multiply --> O(n * n)




