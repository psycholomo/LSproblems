strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

capital = (string.capitalize() for string in strings if len(string) >= 5)

print(set(capital))