
def divide(num1, num2):

    try:
        if not isinstance(num1, int) or not isinstance(num1, int):
            raise ValueError("Will only accept integers")
    except:
        print("number is not divisible by 0")



try:
    num1 = 1
    num2 = 2
    result = num1 / num2
except ZeroDivisionError:
    print("cannot divide by 0")

except ValueError:
    print("enter a valid number")

else:
    print(f"The result is : {result}")

finally:
    print("end of the program")