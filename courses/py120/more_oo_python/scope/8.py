class Car:
    manufacturer = "class"

    def __init__(self):
        self.manufacturer = "instance"
    
    def show_manufacturer(self):
        print("this is the class" + self.__class__.manufacturer)
        print("this is the instance." + self.manufacturer)


new_car = Car()

new_car.show_manufacturer()