
def later(callback, arg):

    def store_state():

        message = callback(arg)
        return message
    return store_state
def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!