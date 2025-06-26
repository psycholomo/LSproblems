

def greetings(lr, obj):
    john_string = " ".join(lr)
    john_title = obj["title"]
    john_occupation = obj["occupation"]

    return f"Hello, {john_string}! Nice to have a {john_title} {john_occupation} around."
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)    

print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.