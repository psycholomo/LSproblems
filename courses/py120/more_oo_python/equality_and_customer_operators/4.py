class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        if isinstance(self, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(self, other):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, self):
            return Vector(self.x * other.x,self.y * other.y)
    def __str__(self):
        return f'Vector({self.x}, {self.y})'

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)
print(my_vector)                      # Vector(8, 16)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 9)

print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'