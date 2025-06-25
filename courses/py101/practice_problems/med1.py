#1

# def flinstones():
#     count = 0
#     myString = "The Flinstones Rock!"
#     while count < 10:
#         myString = "-" + myString
#         print(myString)
#         count += 1

# for padding in range(1, 11):
#     print(f'{"-" * padding}The Flinstones Rock!')
# flinstones()


def factors(number):
    divisor = number
    result = []
    while divisor >= 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result



def last_element(my_list):

    return my_list[-1]

my_list = [1, 5, 3, 7]

print(last_element(my_list) == 7)  # True
print(my_list == [1, 5, 3, 7])     # False