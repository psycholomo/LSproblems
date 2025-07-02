
'''
if the len of the arr is 1 or less, return the original input
in order to divide the array in half we can find the middle by taking the length
and dividing by 2
we can then slice the array with the middle
find the first half up to the second,
and second to last

'''

def halvsies(arr):
    middle = len(arr) // 2
    if len(arr) == 1:
        return [arr, []]
    if len(arr) == 0:
        return [[], []]
    first_half = arr[0:middle]
    second_half = arr[middle:len(arr)]
    if len(arr) % 2 == 0:
        return [first_half, second_half]
    
    first_half = arr[0: middle +1]
    second_half = arr[middle + 1:len(arr)]
    return [first_half, second_half]


print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

#more elegegant solution

def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]