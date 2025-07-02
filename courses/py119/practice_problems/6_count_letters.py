'''
we need to check if the letter is an actual alphabetical letter
we also need to only check against lower letters
if the letter is lower,
add to dict
split the string into a list
loop through that list,
check to see if the letter is lowercase
check to make sure its actually aplhabetical
return a hash map with counts of all lowercase letters
'''


def count_letters(word):
    word_list = word.split()
    return_dict = {}
    for my_word in word_list:
        for letter in my_word:
            if letter.isalpha() and letter == letter.lower():
                if letter in return_dict:
                    return_dict[letter] += 1
                else:
                    return_dict[letter] = 1
    return return_dict

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})