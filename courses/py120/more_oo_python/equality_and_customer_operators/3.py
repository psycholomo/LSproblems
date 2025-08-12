class Cat:
    def __init__(self, name):
        self.name = name
    
    def __gt__(self, other):
        if isinstance(other, Cat):
            return self.name.casefold() > other.name.casefold()
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Cat):
            return self.name < other.name
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.name == other.name
        return NotImplemented
    
    def __ne__(self, value):
        if isinstance(value, Cat):
            return self.name != value.name
        return NotImplemented