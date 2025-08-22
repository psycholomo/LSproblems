from functools import reduce
my_strings = ['abc','def','hi']

concat = reduce(lambda x, y : x + y, my_strings)

print(concat)