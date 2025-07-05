'''
Create a function that takes a list of integers as an argument. Determine and return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.
'''

'''
the number when we choose an index is not included in the sum
Because of this, we can slice this in to two halves,
sum the two halves,
if the two halves are equal, return the index that we are on

loop through the array once,
slice it based on the current index that we are
first half is from 0 to index (which will exclude current)
second half is from index + 1 to end of slice

if nothing is equal,
return -1

'''

def equal_sum_index(arr):

    for i in range(len(arr)):
        slice1 = arr[0:i]
        sum1 = sum(x for x in slice1)
        slice2 = arr[i + 1:]
        sum2 = sum(x for x in slice2)
        print(f'sum1 {slice1}')
        print(f"sum2 {slice2}")
        if sum1 == sum2:
            return i
    
    return -1



# print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # The following test case could return 0 or 3. Since we're
# # supposed to return the smallest correct index, the correct
# # return value is 0.
# print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)