#rock paper scissors
#play against a computer
# take user input
# evaluate who won 
# 
import random
def prompt(input):
    print(f"==>{input}")

input_dict = {
    "r" : ["sc", "l"],
    "sp" : ["sc", "r"],
    "sc" : ["p", "l"],
    "l" : ["sp", "p"],
    "p" : ["r", "sp"],
    }

def prompter(message):
    prompt(message)
    my_message = input()

    while True:
        if check_valid(my_message):
    
            break
        else:
            prompt("you entered an invalid input, try entering again")
            my_message = input()
    return my_message

def check_valid(input):

    try:
        if input not in input_dict.keys():
            raise ValueError("Must select from valid input")
    except ValueError:
        return False
    
    return True

def find_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Its a tie"
    if player_choice in input_dict[computer_choice]:
        return "computer won"
    else:
        return "player won"



print("Welcome to rock paper scissors, choose 'r' for rock, 'sp' for spock" \
"'sc' for scissors, 'l' for lizard and 'p' for paper")
myValue = prompter("please select a value")
computer_value = list(input_dict.keys())

computer_choice = random.choice(computer_value)
prompt(f"The computer chose {computer_choice}")
prompt(f"You chose {myValue}")
prompt(find_winner(myValue, computer_choice))

#computer_selected = computer_value.