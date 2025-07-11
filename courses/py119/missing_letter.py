'''
input is all lowercase
output is the letters that are not in the word

'''

def missing_letters(word):

    return_list = []

    letter_list = list('abcdefghijklmnopqrstuvwxyz')
    for letter in word:
        if letter in letter_list:
            letter_list.remove(letter)

    

    return "".join(letter_list)



print(missing_letters('the quick brown fox'))

# input: "the quick brown fox"
# output: "adgjlmpsvxyz"
