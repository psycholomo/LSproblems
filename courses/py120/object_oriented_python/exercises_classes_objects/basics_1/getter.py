class Cat():
    def __init__(self, name):
        self._name = name


    def greet(self):
        print(f"Hello my name is {self._name}")
        
    @property
    def name(self):
        return self._name
kitty = Cat("kitty")
kitty.greet()