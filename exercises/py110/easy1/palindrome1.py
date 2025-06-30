
#we should be able to just reverse the string 
#if the reversed string is the same as the original string, return true
def is_palindrome(string):
    reversed_string = string[::-1]

    return reversed_string == string




print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)