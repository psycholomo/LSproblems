# =begin
# Unique String Characters
# Given two strings, return the characters that are not common in the two strings.

'''
the input is two strings
the output are all of the characters not common in the two strings
the output will be the characters from the first string followed by the second string
loop through each character in the first 
check to see if it is in the second string
we can then loop through the second string and see if any characters in the first string were not visited
we can use a set to see if any chracters were missed or are already there
edge case is if the character is length of 1, return the strings concatenated
if everything matches, return empty string
'''

def unique_string_characters(string1, string2):
    result_string = ""
    visisted_strings = []

    for char in string1:
        if char not in string2:
            result_string += char
            visisted_strings.append(char)
    
    for char in string2:
        if char not in string1 and char not in visisted_strings:
            result_string += char
            visisted_strings.append(char)
    return result_string      

# Python test cases
print(unique_string_characters("xyab","xzca") == "ybzc") #// true
print(unique_string_characters("a","z") == "az") #// true
print(unique_string_characters("abcd","de") == "abce") #// true
print(unique_string_characters("abc","abba") == "c") #// true
print(unique_string_characters("xyz","zxy") == "") #// true


#=end

messed_pokemon = 'BulbAsaur-ChaRMAndeR-pikaCHU-chariZard-SQuirtlE'

# add your code here
pokedex = messed_pokemon.split("-")
for i in range(len(pokedex)):
    pokedex[i] = pokedex[i].capitalize()
del pokedex[3] 

print(pokedex) # ['Bulbasaur', 'Charmander', 'Pikachu', 'Squirtle']`