'''
create a dictionary of values that maps the word to the number

split the word into each word

loop through the list
if the word is in the dictionary
replace the word with the number in the list

join the list together
return the newly created string
'''

def word_to_digit(message):
    words = message.split()
    my_dict = {"zero": "0",
               "one": "1",
               "two": "2",
               "three": "3",
               "four":"4",
               "five": "5",
               "six": "6",
               "seven": "7",
               "eight": "8",
               "nine": "9"}
    
    for indx, word in enumerate(words):
        if word in my_dict:
            words[indx] = my_dict[word]
    
    return " ".join(words)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True