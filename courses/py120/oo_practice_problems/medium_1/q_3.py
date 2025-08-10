class Animal:
    def __init__(self):
        pass
    def speak(self, message):
        print(message)

class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    
    def bark(self):
        self.speak("Woof! Woof!")


myDog = Cat()
myDog.meow()