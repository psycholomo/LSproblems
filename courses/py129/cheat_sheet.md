can bypass encapsulation and name mangling by using the obj.__Dog__breed

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


def __eq__(self, other):
        if isinstance(other, Cat):
            return self.name == other.name
        return NotImplemented
    
def __ne__(self, value):
        if isinstance(value, Cat):
            return self.name != value.name
        return NotImplemented