#1

class Car():
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color
    

    def __str__(self):
        return f"{self.color} {self.year} {self.name}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.year},{self.color})"



vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')