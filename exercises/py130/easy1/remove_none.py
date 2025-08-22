lists = [1,2,3,None,5]

results = filter(lambda x : x is not None, lists)

print(list(results))