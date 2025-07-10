# Example:
# input: [1, 2, 0, 2]
# output: [1, 1, 2, 0]  # 0 appears once, 1 once, 2 appears twice, 3 not at all

'''
Create a function that returns a new list in which 
each element is the number of times the corresponding 
index appears as a value in the original list.


create a key that is the index, and values that are the count
return the list of the count
'''

def reverse_index(list):

    my_dict = {}

    for indx, value in enumerate(list):
        my_dict[indx] = 0
    

    for value in list:
        if value in my_dict:
            my_dict[value] += 1
    

    return list(my_dict.values())


print(reverse_index([1,2,0,2]))