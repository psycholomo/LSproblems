class NegativeNumberError(Exception):
    pass

num = float(input('enter a number: '))

if num < 0:
    raise NegativeNumberError("negative numbers are not allowed")


try:
    num1 = 1
    num2 = 2
    result = num1 / num2
except (ZeroDivisionError, ValueError) as e:
    print(e)

else:
    print(f"The result is : {result}")

finally:
    print("end of the program")