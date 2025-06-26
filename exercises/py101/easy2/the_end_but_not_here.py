
def penultimate(string):
    string_arr = string.split(" ")
    return string_arr[-2]
    


# These examples should print True
print(penultimate("last word"))
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")