#Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.


'''
to pull out the value we need to use modulo  by %10
to get the new value we need to divide the number by floor of 10
while the number is greater then 0
pull out the new value, convert it to a string
append to a new string
because this will be at the end we need to reverse the string at the end
if number because less then or equal to 0,
return the new built string in reverse


'''
def integer_to_string(num):
    if num < 10:
        return str(num)
    convert_str= ""
    convert_num = num
    

    while convert_num > 0:
        new_num = convert_num % 10
        convert_str += str(new_num)
        convert_num = convert_num // 10
    
    return convert_str[::-1]

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True


print(10 // 10 )