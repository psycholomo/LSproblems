
def multiplicative_average(num_arr):
    length = len(num_arr)
    multiple_numbers = 1

    for num in num_arr:
        multiple_numbers *= num
    
    return_num = multiple_numbers / length

    return f'{return_num:.3f}'



print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")