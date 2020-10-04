def countingValleys(steps, path):
    
    sea_level = 0
    counter = 0

    for item in path:
        if item == "U":
            sea_level += 1
            if sea_level == 0:
                counter += 1
        elif item == "D":
            sea_level -= 1
    
    return counter

print(countingValleys(8, "UDDDUDUU"))