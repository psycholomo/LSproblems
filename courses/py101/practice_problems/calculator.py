def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str) or float(number_str)
    except ValueError:
        return True
    
    return False

def prompter(message):
    prompt(message)
    user_input = input()

    while invalid_number(user_input):
        prompt("Hmm... that doesn't look like a valid number.")
        user_input = input()
    
    return float(user_input)
    # returns the input in a float format


prompt("Welcome to Calculator!")
def calculator():
        
    first_num =prompter("Whats the first number?")

    second_num = prompter("Whats the second number?")

    prompt("What operation would you like to perform\n1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    while operation not in ["1","2","3","4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()


    match operation:
        case "1":
            output = first_num + second_num
        case "2":
            output = first_num - second_num
        case "3":
            output = first_num * second_num
        case "4":
            output = first_num / second_num

    prompt(f"The result is {output}")


while True:
    calculator()
    prompt("Would you like to make another calculation?")
    message = input("type y for yes or n for no")
    if message == "y":
        calculator()

    elif message == "n":
        prompt("thanks for using the calculator")
        prompt("goodbye")
        break
    
    else:
        prompt("Enter a valid 'y' or 'n' for the prompt")
