
def digit_list(num):
    return_list = []
    my_num = num

    while my_num > 0:
        append_num = my_num % 10
        return_list.append(append_num)
        my_num //= 10
    print(return_list)
    return return_list[::-1]
    

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# simpler solution
# return [int(digit) for digit in str(number)]
# or
# for n in str(num):
# new_list.append(int(n))