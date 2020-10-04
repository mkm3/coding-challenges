def sockMerchant(n, ar):

    pair_count = defaultdict(int)
    counter = 0  
    
    for key in ar:
        if pair_count[key] == 1:
            counter += 1
            pair_count[key] = 0
        else: 
            pair_count[key] += 1
    return counter

print(sockMerchant(n, [10 20 20 10 10 30 50 10 20]))