def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    #create jumps counter
    counter = 0
    #set an i variable to keep track of branch position
    i = 0

    if len(branches) <= 1:
        return 0

    if len(branches) == 2 or len(branches) == 3:
        return 1
    #setup while loop
    while i < len(branches) - 1: # we minus 1 to ignore the last element in array and to avoid out of range error
        #setup if statement
        if i < len(branches) - 2 and branches[i + 2] == 0: # we minus 2 to ignore the last two element in array and to avoid out of range error
            i += 2
        #setup else statement
        else:
            i += 1
        #increment jumps counter at every hop
        counter += 1

    #return counter
    return counter


print(lemur([0])) # 0
print(lemur([0, 0])) # 1
print(lemur([0, 0, 0])) # 1 
print(lemur([0, 1, 0])) # 1
print(lemur([0, 0, 1, 0])) # 2
print(lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])) # 5
print(lemur([0, 0, 1, 0, 0, 1, 0])) # 4
print(lemur([0, 0, 0, 0, 1, 0])) # 3
print(lemur([0, 0, 0, 1, 0, 0])) # 3
