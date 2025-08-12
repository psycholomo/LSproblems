class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    @width.setter
    def width(self, new_width):
        if isinstance(new_width, int) and new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be a positive integer")
rectangle = Rectangle(3, 7)
print(rectangle.width, rectangle.height)      # 3 7

rectangle._width = 8
print(rectangle.width)
# AttributeError: property 'width' of 'Rectangle' object
# has no setter