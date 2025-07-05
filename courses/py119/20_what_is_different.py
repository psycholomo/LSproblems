'''
this is another loop through
get the count
if the count is only 1
return the value
'''

def what_is_different(nums):

    my_count = {}

    for num in nums:
        if num in my_count:
            my_count[num] += 1
        else:
            my_count[num] = 1
    

    for key, value in my_count.items():
        if value == 1:
            return key


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)