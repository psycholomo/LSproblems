strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def capitalize(strings):
    for string in strings:
        yield string.capitalize()
    