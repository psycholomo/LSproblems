user_input = input("What is your name?")

greeting = f"Hello {user_input}"
yelling_input = f"HELLO {user_input.upper()} WHY ARE WE YELLING?"
if user_input.endswith("!"):
    print(yelling_input)
else:
    print(greeting)