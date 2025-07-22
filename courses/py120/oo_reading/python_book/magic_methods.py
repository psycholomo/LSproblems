#1
from math import sqrt
class Car():
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color
    

    def __str__(self):
        return f"{self.color} {self.year} {self.name}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.year},{self.color})"



# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x * other.x
        new_y = self.y * other.y

        return Vector(new_x, new_y)
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    # __iadd__ method omitted; we don't need it for this exercise

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)


# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0


class Candidate():
    def __init__(self, name):
        self.name = name
        self._votes = 0
    
    @property
    def votes(self):
        return self._votes
    

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError("must be an integer")
        self._votes += other
    
    def __str__(self):
        return f"{self.name}: {self.votes} votes"


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = [
    mike_jones,
    susan_dore,
    kim_waters,
]

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

class Election():
    def __init__(self, canidates):
        self.canidates = canidates
    
    def results(self):
        winner = 0
        winner_name = ""
        for canidate in self.canidates:
            if canidate.votes > winner:
                winner = canidate.votes
                winner_name = canidate.name
        total_votes = self.num_of_votes(self.canidates)
        percentage = (winner / total_votes) * 100
        print(total_votes)
        print(winner)

        print(f"{winner_name} won: {percentage:.2f}% of votes")

        

    def num_of_votes(self, list_of_nums):

        total = 0
        for num in list_of_nums:
            total += num.votes
        return total
print(mike_jones)
election = Election(candidates)
election.results()