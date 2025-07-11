'''
best way to solve this is with a set
we only want the first instance of each word
so we can loop through the list
and add the word to the set if its not in there
make sure everything is compared in lowercase letters
We can then return the set as order may not matter

'''

def clean_room(list_of_words):

    my_set = set()
    return_list = []
    for word in list_of_words:
        lower_word = word.lower()
        if lower_word not in my_set:
            return_list.append(word)
            my_set.add(lower_word)
    
    return return_list

input = ['Hello', 'world', 'hello', 'World']
# output: ['Hello', 'world']
print(clean_room(input))