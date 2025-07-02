'''
get a count of all numbers
loop through all the numbers and divide by // 2
add that number to a running total of count for pairs
return total count
'''

def pairs(arr_num):
    count = 0
    num_dict = {}

    for num in arr_num:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    for value in num_dict.values():
        equate = value // 2
        count += equate
    
    return count


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)