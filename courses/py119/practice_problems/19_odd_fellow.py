'''
loop through each element in the list
get a count for each element, using a hashmap

go through the values in the hashmap
if one of the values % 2 == 1
return the value
'''

def odd_fellow(arr):
    my_map = {}

    for i in arr:
        if i not in my_map:
            my_map[i] = 1
        else:
            my_map[i] += 1
    
    for key, value in my_map.items():
        if value % 2 == 1:
            return key
    

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)