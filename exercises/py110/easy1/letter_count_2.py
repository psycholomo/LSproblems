

def word_sizes(string):

    string_arr = string.split()
    cleaned_word_list = []
    print(string_arr)
    return_dict = {}
    for word in string_arr:
        char_list = list(word)
        clean_word = ""
        for char in char_list:
            if char.isalpha():
                clean_word += char
        
        cleaned_word_list.append(clean_word)
        clean_word = ""

    for word in cleaned_word_list:
        word_length = len(word)
        if len(word) not in return_dict:
            return_dict[word_length] = 1
        else:
            return_dict[word_length] += 1
    
    return return_dict
    '''
    split each word into a list
    then split each charcter
    check to see if the character is alphanumeric
    if it is push it into a placeholder list
    join the list
    get the length of the string without the strange characters in it

    '''

    print('w@ll'.isalnum())
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})