# # add some code here
# class Dog:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
    
    
#     @property
#     def name(self):
#         return self._name
#     @property
#     def age(self):
#         return self._age
#     @staticmethod
#     def bark():
#         print("Woof! Woof!")
# fido = Dog('Fido', 5)
# paws = Dog('Paws', 3)

# print(fido.name)              # Fido
# print(paws.name)              # Paws
# print(fido.age)               # 5
# print(paws.age)               # 3

# fido.bark()                   # Woof! Woof!
# paws.bark()                   # Woof! Woof!

# try:
#     fido.name = 'Barni'
# except AttributeError as e:
#     print(f"Error: {e}")      # prints error message

# try:
#     paws.age = 4
# except AttributeError as e:
#     print(f"Error: {e}")      # prints error message

# class FlyingMixin:
#     def fly(self):
#         return f"{self.name} is flying"

# class Bird():
#     pass

# class Penguin(Bird):
#     pass

# class Swan(FlyingMixin, Bird):
#     pass

# class Insect(FlyingMixin):
#     pass


# class Chef:
#     def prepare_wedding(self, wedding):
#         print(f"Prepare food for {wedding.guests}")


# class Musician:
#     def prepare_wedding(self, wedding):
#         print(f"Prepare these songs for {wedding.songs}")


# mychef = Chef()
# myMuscian = Musician()

# for preparers in [mychef, myMuscian]:
#     preparers.prepare_wedding(wedding)

# class BankAccount:
#     bank_accounts = 0
    

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#         self.__class__.bank_accounts += 1

#     def get_balance(self):
#         return self.balance
    
 

# sally = BankAccount("Sally", 300) #initialzes a new bankaccount object named sally with a balance of 300
# frank = BankAccount("Frank", 0) #initialzes a new bankaccount object named Frank with a balance of 0

# frank.balance = 15
# sally. balance = 350

# print(frank.balance)
# print(sally.balance)


# class Foo:
#     def __init__(self, bar, qux):
#         self._bar = bar
#         self._qux = qux
    
#     @property
#     def bar(self):
#         return self._bar
    
#     def qux(self):
#         return self._qux

# foo = Foo(1, 2)

# print(foo.bar)      # 1
# foo.bar = 3
# print(foo.bar)      # 3
# print(foo.qux)      # 2

# try:
#     foo.qux = 4
# except AttributeError as e:
#     print(f"Error: {e}")      # prints an error message


# class Car:
#     def __init__(self, speed):
#         self.speed = speed

#     @property
#     def speed(self):
#         return self._speed

#     @speed.setter
#     def speed(self, value):
#         self._speed = value

#     def accelerate(self):
#         new_speed = self.speed + 10
#         speed = new_speed

#     def is_faster_than(self, other_car):
#         return self.speed >= other_car.speed

# # Testing the Car class
# car1 = Car(40)
# car2 = Car(40)
# car1.accelerate()
# print(car1.is_faster_than(car2))

# class Person:
#     people = 0
#     def __init__(self):
#         self.__class__.people += 1
    
#     @classmethod
#     def total_people(cls):
#         return cls.people
# bob = Person()
# alice = Person()
# print(Person.total_people())     # this should print 2


# class Person:
#     def __init__(self, name, weight, height):
#         self._name = name
#         self._weight = weight
#         self._height = height

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, other):
#         self._name = other
    
#     @property
#     def weight(self):
#         return self._weight
    

#     @weight.setter
#     def weight(self, value):
#         self._weight = value

    
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,other):
#         self._height = other
#     def __iadd__(self, value):
#         if isinstance(value, int) or isinstance(value, float):
#             self._weight += value
#             self._height += value



# susan = Person('susan', 123, 64)
# print(f'{susan.name} {susan.weight} {susan.height}')
# # susan 123 64

# susan.name = susan.name.capitalize()
# susan.weight += 2
# susan.height += 0.5

# print(f'{susan.name} {susan.weight} {susan.height}')
# # Susan 125 64.5


# class ColorIntensity:

#     def __init__(self, intesity_level):
#         if intesity_level < 0 or intesity_level > 255:
#             raise ValueError("The value needs to be between 0 and 255")
#         else:
#             self.intensity_level = intesity_level
        
#     def __eq__(self, other):
#         if isinstance(other, ColorIntensity):
#             return self.intensity_level == other.intensity_level

#     def __gt__(self, other):
#         if isinstance(other, ColorIntensity):
#             return self.intensity_level > other.intensity_level
#     def __lt__(self, other):
#         if isinstance(other, ColorIntensity):
#             return self.intensity_level < other.intensity_level

# ci1 = ColorIntensity(100)
# ci2 = ColorIntensity(150)
# ci3 = ColorIntensity(100)

# try:
#     ci4 = ColorIntensity(256)
# except ValueError as e:
#     print(f"Error: {e}")      # Prints an error message

# try:
#     ci5 = ColorIntensity(-1)
# except ValueError as e:
#     print(f"Error: {e}")      # Prints an error message

# print(ci1 < ci2)    # True
# print(ci1 == ci2)   # False
# print(ci3 == ci1)   # True
# print(ci3 > ci1)    # False
# print(ci2 > ci3)    # True

# class Student:
#     def __init__(self, name, grade):
#         self._name = name
#         self._grade = grade
    
#     def __eq__(self, other):
#         if isinstance(other, Student):
#             if self._name == other._name and self._grade == other._grade:
#                 return True
#         return False

# bob1 = Student('Bob', 12)
# bob2 = Student('Bob', 12)
# print(bob1 == bob2)             # False


# class Counter:
#     def __init__(self, num=0):
#         self._value = num
    
#     @property
#     def value(self):
#         return self._value
    
#     def increment(self, increment_value):
#         self._value += increment_value
    
#     def decrement(self, decrement_value):
#         self._value -= decrement_value
    
#     def __add__(self, other):

#         return Counter(self._value + other._value)

#     def __str__(self):
#          return f"{self._value}"

# c1 = Counter()
# c2 = Counter()
# c1.increment(3)
# c2.increment(5)
# c1.decrement(1)

# result = c1 + c2
# print(result)                 # 7

# # try:
#     c1.value += 1
# except AttributeError as e:
#     print(f"Error: {e}")      # Prints error message

# try:
#     c1 = c1 + 1
# except TypeError as e:
#     print(f"Error: {e}")      # Prints error message



class DelegateMixin:
    def delegate(self, worker):
        print(f"delegating task to {worker._name}")

class Employee:
    def __init__(self, name, serial_number):
        self._name = name
        self._serial_number = serial_number
        self.desk = None
        self.vacation_days= None

    def __str__(self):
        return (f"Name:{self._name}\n"
                f"Type: {self.__class__.__name__}\n"
                f"Serial Number: {self._serial_number}\n"
                f"Vacation days: {self.vacation_days}\n"
                f"Desk: {self.desk}")
    

class FullTimeEmployee(Employee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        
    def take_vacation(self):
        print("taking vacation")


class PartTimeEmployee(Employee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        self.vacation_days = 0
        self.desk = "Open workspace"

class RegularEmployee(FullTimeEmployee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        self.vacation_days = 10
        self.desk = "Cubicle"


class Manager(DelegateMixin, FullTimeEmployee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        self.vacation_days = 14
        self.desk = "private office"


class Executive(DelegateMixin, FullTimeEmployee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        self.vacation_days = 20
        self.desk = "corner office"
    
    def hire(self, employee):
        pass

    def fire(self, employee):
        pass


dave = Manager("Dave", "123456789")
print(dave)
print()

alice = Executive("Alice", "987654321")
print(alice)
print()

bob = RegularEmployee("Bob", "555666777")
print(bob)
print()

carol = PartTimeEmployee("Carol", "111222333")
print(carol)