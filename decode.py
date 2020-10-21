def decode(s):
    """Decode a string."""

    #create empty string ""
    new_s = ""

    #var for string iteration
    idx = 0

    #iterate through length of s
    while idx < len(s):

        #if you hit an int...the integers you hit in s will tell you how many letters to skip
        num_to_skip = int(s[idx])

        #to find the letter we need to grab
        idx += num_to_skip + 1

        #take the last letter and add it to var for string
        new_s += s[idx]

        #move over 1 idx to get evaluate new char
        idx += 1

    #return new string
    return new_s




print(decode("0h")) #'h'
print(decode("2abh")) #'h'
print(decode("0h1ae2bcy")) #'hey'