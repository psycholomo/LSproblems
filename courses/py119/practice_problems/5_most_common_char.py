'''
join the string so there are no spaces and make all characters lower case
loop through the string for every character and create a hashmap with the letter and count
record a max number from the hashmap values

loop through the string again and if the key value is max, return that value

'''
def most_common_char(word):
    my_map = {}
    
    squished_word = "".join(word.lower().split())
    for char in squished_word:
        if char in my_map:
            my_map[char] += 1
        elif char.isalpha():
            my_map[char] = 1
    
    max_number = max(my_map.values())

    for char in squished_word:
        if my_map[char] == max_number:
            return char

    


print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

