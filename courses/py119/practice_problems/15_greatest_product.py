'''
we can use a range and slicing to always return 4 elements
the calculation will be from the num to num + 4
this will give us the slice we need for every number
we can then seperate out 4 numbers into a list
convert each num to an integer
calculate the product of that integer
then compare it to a max, if it is greater replace the max

return max number
'''

def greatest_product(str_num):
    "do math here"
    my_slice = slice_string(str_num)
    my_max = 0
    for num in my_slice:
        running_total = 1
        for char in num:
            int_char = int(char)
            running_total *= int_char
        my_max = max(running_total, my_max)
    
    return my_max



def slice_string(string):
    string_slices = []

    for i in range(len(string)):
        my_slice = string[i:i+4]
        if len(my_slice) == 4:
            string_slices.append(my_slice)

    return string_slices

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6