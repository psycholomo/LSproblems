#Given a list of positive integers,
#  return a dictionary grouping them by
#  number of digits.

'''
convert each number into a string
get the length of each string
if the length exists as a key in a dictionary
append it to that dictionary list
otherwise create a new dictionary list with the length
as the key
return the dictionary
'''

def group_sums(num_list):

    return_dict = {}

    for num in num_list:
        str_num = str(num)
        length = len(str_num)

        if length not in return_dict:
            return_dict[length] = []
            return_dict[length].append(str_num)
        else:
            return_dict[length].append(str_num)
    return return_dict

input = [1, 23, 456, 12, 7890, 3]

print(group_sums(input))

# output: {1: [1, 3], 2: [23, 12], 3: [456], 4: [7890]}
