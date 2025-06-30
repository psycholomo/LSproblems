
'''
loop through the string and check to see if it is alphanumeric,
if it is push it to an array
join the array to make all one string without spaces
check to see if it is a palindrome
'''
def is_real_palindrome(string):
    my_arr = []
    for char in string:
        if char.isalnum() and char.isascii():
            my_arr.append(char.casefold())
   
    string ="".join(my_arr)

    return is_palindrome(string)





def is_palindrome(string):
    reversed_string = string[::-1]

    return reversed_string == string

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True