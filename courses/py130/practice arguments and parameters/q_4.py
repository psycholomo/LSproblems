def calculate_average(*args):
    print(args)
    average = 0
    if len(args) < 1:
        return None
    for num in args:
        average += num
    
    return average/len(args)

print(calculate_average(1,2,3,4))