def concatenate(*args):
    string = ""
    for value in args:
        string += " " + value
    return string
print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course