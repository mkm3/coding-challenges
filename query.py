def valid_names(n1, q1):
    
    valid_names = []

    for name in n1:
        for prefix in q1:
            if prefix in name:
                if len(prefix) == len(name) and prefix == name:
                    pass
                else:
                    valid_names.append(name)
    return len(valid_names)

print(valid_names(["jackie", "joey", "joe", "jenny"], ["joe"]))