def multiply_list(list1, list2):
    return_list = []
    for num in range(len(list1)):
        mul_num = list1[num] * list2[num]
        return_list.append(mul_num)
    
    return return_list

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True