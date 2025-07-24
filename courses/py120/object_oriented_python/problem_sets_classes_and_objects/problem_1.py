
class Person():
    def __init__(self, name):
        self.name = name
    

bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert