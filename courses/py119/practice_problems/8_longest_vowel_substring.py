'''
the best option for this problem is two pointers
create a list that has vowels
loop through until you find a vowel.
check the next character to see if it is also a vowel, and any subsequent characters
if it is not a vowel, return the length 
pointers will start at position 0, and position 1
move the first pointer until we hit a vowel.
then move the second pointer until its a constant or end of the string
continue doing this until we have the longest vowel

a better way to tackle this problem, as we dont need the elements but just the count
loop through and increase the count by 1 if it is a vowel,
if its not, set the count to 0
set max to highest count
'''

def longest_vowel_substring(string):
    max_num = 0
    vowels = "aeiou"
    counter = 0
    for char in string:
        if char in vowels:
            counter += 1
        else:
            max_num = max(counter, max_num)
            counter = 0
        
        max_num = max(counter, max_num)
    return max_num








print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)