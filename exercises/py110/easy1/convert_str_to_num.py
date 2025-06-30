'''
convert string to a int without using any of the standard libraries
need to calculate each individual number with a hash that ties the number to a string
{"1" = 1} for example
we then need to find the placeholder of each number
if we work right to left through the string. we can take the 1's place. then the next number will be
the number * 10, then numer * 100, etc

knowing this lets reverse the string,
split the string in a list
get the value out of a hashback
on first iteration multiple by 1 and add to a number
then by 10, 100 etc
until we are at end of number

'''

def string_to_integer(input_str):
    reversed_str = input_str[::-1]
    string_arr = list(reversed_str)
    num_multiplier = 0
    return_num = 0
    num_table = {
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "0":0,
    }

    for indx,num in enumerate(string_arr):
        if indx == 1:
            num_multiplier = 10
        value = num_table.get(num)
    
        if value == 0:
            return_num += num_multiplier
        
        elif indx == 0:
            return_num += value
        else:
            return_num += value * num_multiplier
        num_multiplier = num_multiplier * 10
    return return_num




print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True



def hexadecimal_to_integer(str_input):
    num_table = {
        "0": 0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    my_string = str_input[::].upper()
    return_value = 0
    for char in my_string:
        return_value = (16 * return_value) + num_table[char]
    print(return_value)
    return return_value



print(hexadecimal_to_integer('4D9f') == 19871)  # True