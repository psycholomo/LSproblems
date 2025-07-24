class Person():
    def __init__(self, name):
        self.name = name
  
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @name.setter
    def name(self, name):
        parts = name.split()
        if len(parts) > 1:
            self._name = name
            self._first_name = parts[0]
            self._last_name = parts[1]
        else:
            self._name = parts[0]
            self._first_name = parts[0]
            self._last_name = ""
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError("Needs to be a valid string")
        if first_name == "":
            raise TypeError("cannot be an empty string")

        self._first_name = first_name     
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError("needs to be a valid string")

        
        self._last_name = last_name

    def __str__(self):
        return self.name

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams