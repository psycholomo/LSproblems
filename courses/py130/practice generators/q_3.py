str_list = ['abc','def','ghi','jkl']

capitlize = (string.capitalize() for string in str_list)

new_item = (tuple(capitlize))
print(str_list)
print(new_item)