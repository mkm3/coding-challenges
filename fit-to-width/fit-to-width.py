"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    #create a reversed stack 'words'
    words = list(reversed(string.split()))

    #create an empty lines list to hold elements
    #elements are lines of a valid char count, element <= n
    lines = []

    #empty list to keep track of the current line
    curr_line = []
    #while there are still words in our words list
    while words:
        #word = last word in list
        word = words[-1] 
        #if length of (curr_line + word) is <= limit  
        if len(' '.join(curr_line + [word])) <= limit:
            #append word to curr_line
            #and pop off the last word on the words list
            curr_line.append(words.pop())

        #if length "" is > limit:
        else:
            # if curr_line: (not necessary)
            #append curr_line to lines list, join with a space
            lines.append(' '.join(curr_line))
            #reset curr_line to empty list
            curr_line = []
    
    lines.append(' '.join(curr_line))
    
    for line in lines:
        print(line)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
