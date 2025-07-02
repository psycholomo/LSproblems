def interleave(list1,list2):
    return_arr = []

    for i in range(len(list1)):
        return_arr.append(list1[i])
        return_arr.append(list2[i])
    return return_arr

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True