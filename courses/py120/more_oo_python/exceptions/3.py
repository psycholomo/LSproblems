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