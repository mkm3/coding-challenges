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
    while i < len(branches) - 1: #we are ignoring last element in array
        #setup if statement
        if branches[i + 2] == 0:
            i += 2
        #setup else statements
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
print(lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])) #5
