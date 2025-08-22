
def greet(name, greeting,/, punc="."):

    return f"{greeting}, {name}{punc}"

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good morning, Pete!