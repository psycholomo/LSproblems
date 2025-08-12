class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

dog1 = Dog('Golden Retriever')
dog2 = Dog('Poodle')

dog1._breed = "something else"
print(dog1._breed)

print(dog1.get_breed())  # Golden Retriever
print(dog2.get_breed())  # Poodle

class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"

cat = Cat()
print(cat.get_name())  # Name not set!
