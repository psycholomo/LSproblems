'''
input is a string

output is a boolean

initial thought is we create a list with all of the alphabetical letters
we can then loop through every character in the input string
if the character is in the list
delete the character in the alphabet list
at the end check to see if the alphabet list is empty
if it is return True
'''

def is_pangram(string):
    alpha_list = list('abcdefghijklmnopqrstuvwxyz')
    print(alpha_list)

    for char in string:
        if char in alpha_list:
            alpha_list.remove(char)
    
    if len(alpha_list) == 0:
        return True
    
    return False

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)