def later2(callback, arg):

    def inner(minutes):
        return callback(arg, minutes)

    return inner 



def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!