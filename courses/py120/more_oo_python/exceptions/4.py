class NegativeNumberError(Exception):
    pass

num = float(input('enter a number: '))

if num < 0:
    raise NegativeNumberError("negative numbers are not allowed")


