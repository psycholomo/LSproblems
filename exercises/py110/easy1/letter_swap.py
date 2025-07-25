'''
Given a string of words separated by spaces, write a function 
that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and
 that the string will always contain at least one word. You may also assume that 
 each string contains nothing but words and spaces, and that there are no leading,
   trailing, or repeated spaces.


   
'''

def swap(word):
    '''
    split the string into a list
    make a list out of each word
    change the position of position 0 and position 1  to be mirrors of each other
    set variables to the letters so we dont overwrite what we are doing
    put the swapped word into a list
    return the list as a string joined by white spaces
    '''
    word_list = word.split()
    new_words = []
    for word in word_list:
        char_list = list(word)
        first_char = char_list[0]
        second_char = char_list[-1]
        char_list[0] = second_char
        char_list[-1] = first_char
        new_words.append("".join(char_list))
    return " ".join(new_words)



print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True