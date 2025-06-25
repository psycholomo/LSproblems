def utf16_value(string):
    sum_ = 0
    for char in string:
        sum += ord(char)
    return sum_