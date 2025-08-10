class walkMixin:
    def walk(self):
        return f"{self.name} {self.gait()} forward."

class Person(walkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(walkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(walkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"


mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"