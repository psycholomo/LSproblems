class Cat():
    def __init__(self, name):
        self.name = name


    def greet(self):
        print(f"Hello my name is {self._name}")
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):

        self._name = name

kitty = Cat("kitty")
kitty.greet()
kitty.name = "Sophie"
kitty.greet()