'''
another way to do this that is more time effecient is to create
a hashmap of the first string and the counts of each letter
we then loop through the second word of characters
if the character count is not 0
keep going
otherwise return false

if we reach the end.
return true

'''

def unscramble(string1, string2):
    if len(string1) < len(string2):
        return False

    string1_dict ={}

    for char in string1:
        if char in string1_dict:
            string1_dict[char] += 1
        else:
            string1_dict[char] = 1
    
    for char in string2:
        if char in string1_dict:
            string1_dict[char] -=1
        elif char not in string1_dict:
            return False
        elif string1_dict[char] < 0:
            return False
    
    return True



print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)