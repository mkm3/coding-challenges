def remove_parentheses(s):

    import re

    return re.sub(r'\([^()]*\)', '', s)

    # return s.replace("()", "")
        

print(remove_parentheses("example(unwanted thing)example"))
# >>> "exampleexample"
