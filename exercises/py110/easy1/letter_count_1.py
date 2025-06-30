'''
Write a function that takes a string consisting of zero or more space-separated words 
and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.
'''


'''
split the string into a list
get the length of each string
if it exists in the dictionary, increment the value in the dict by 1
otherwise create a new key and set the value to 1



'''
def word_sizes(string):
    string_split = string.split()
    return_dict = {}
    for word in string_split:
        length_of_word = len(word)

        if return_dict.get(length_of_word) is None:
            return_dict[length_of_word] = 1
        else:
            return_dict[length_of_word] += 1
    
    return return_dict


string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})