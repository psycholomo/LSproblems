
#the first digit is never touched
# have a placeholder with the running total
# add current value with the running total
# in the array place that number
def running_total(int_arr):
    if len(int_arr) <= 1:
        return int_arr
    
    place_num = int_arr[0]
    
    for num in range(1, len(int_arr)):
        place_num += int_arr[num]
        int_arr[num] = place_num

    return int_arr
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])   