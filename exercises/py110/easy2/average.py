def average(my_list):
    total_sum = 0

    for i in my_list:
        total_sum += i
    
    return total_sum // len(my_list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True