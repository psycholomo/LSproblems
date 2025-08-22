strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def capital(string_list):

    for string in string_list:
        if len(string) < 5:
            yield string.capitalize()

#     for string in string_list:
#         yield string.capitalize() if len(string) < 5 else ""

print(set(capital(strings)))