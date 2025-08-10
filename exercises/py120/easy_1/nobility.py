class walkMixin:

    def gait(self):
        return self.walking
    def walk(self):
        return f"{self} {self.gait()} forward."


class Animal(walkMixin):
    def __init__(self,name, walking="saunters"):
        self.name = name
        self.walking = walking
    
    def __str__(self):
        return self.name

class Person(Animal):
    
    def __init__(self, name, walking="strolls"):
        super().__init__(name, walking)

class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name, "struts")

        self.title = title
    
    def __str__(self):
        return f"{self.title} {self.name}"



class Cat(Animal):
    def __init__(self, name, walking="saunters"):
        super().__init__(name, walking)
        

class Cheetah(Animal):
    def __init__(self, name):
        super().__init__(name,"runs")


mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"


byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"