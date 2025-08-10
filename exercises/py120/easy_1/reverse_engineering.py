class Transform:
    def __init__(self, my_string):
        self.my_string = my_string
    
    def uppercase(self):
        return self.my_string.upper()
    @classmethod
    def lowercase(cls, my_string):
        return my_string.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz