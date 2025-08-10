class Cat:
    COLOR = "purple"
    def __init__(self, name):
        self._name = name

    def greeting(self):
        return f"Hello, my name is {self._name} and I am {Cat.COLOR} cat!"      
    
    @property
    def name(self):
        return self._name
    


kitty = Cat("Sophie")
kitty.greeting()