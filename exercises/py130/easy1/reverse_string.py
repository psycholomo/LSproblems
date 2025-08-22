my_string = 'abcdefg'

characters = (my_string[char] for char in range(len(my_string) -1,-1,-1))

finished = "".join(list(characters))
print(finished)