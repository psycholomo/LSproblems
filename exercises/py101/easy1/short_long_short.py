def short_long_short(string1, string2):
    if string1 == "":
        return string2
    elif string2 == "":
        return string1
    
    if len(string1) > len(string2):
        return string2 + string1 + string2

    return string1 + string2 + string1