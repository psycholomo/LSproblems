
def user_input(this= None):
    ticker = False
    while ticker == False:
        try_this = input()
        if try_this == "stop":
            ticker = True
            break
        yield try_this



for what in user_input():
    print(what)