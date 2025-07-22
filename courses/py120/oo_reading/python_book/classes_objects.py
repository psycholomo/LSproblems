#1) create a car class that meets these requirements https://launchschool.com/books/oo_python/read/classes_objects exercises

class ColorMixin():
    def paint(self, color):
        self._color = color
        print(f"the color is now {self.color}")
    
    def get_color(self):
        print(f"the color is {self.color}")

class Car(ColorMixin):

    def __init__(self, model, model_year, color):
        self.speed = 0
        self._model = model
        self._model_year = model_year
        self.color = color
        self.engine = "Off"
      

    @classmethod
    def gas_mileage(cls, distance_traveled, fuel_burned):
        return (distance_traveled / fuel_burned) if fuel_burned > 0 else 0
    @property
    def model(self):
        return self._model
    
    @property
    def model_year(self):
        return self._model_year
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("Color must be a string")
        if color == "":
            raise ValueError("You must provide a valid string")
        
        self.paint(color)

    def start(self):
        if self.engine == "Off":
            print("Starting the engine")
            self.engine = "On"
        else:
            print("The engine is already on")

    def stop(self):
        if self.engine == "On":
            print("stopping the engine")
            self.speed = 0
            self.engine = "Off"
        else:
            print("The engine is already off")    

    def accelerate(self):

        if self.engine == "On":
            self.speed += 10
        
        else:
            print("you need to start the car first")

    def brake(self, number):
        self.speed -= number
        print(f'You decelerated {number} mph.')
    

    def get_speed(self):
        print(f"your speed is {self.speed} mph")

class Person:
    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)
    
    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()

        return f'{first_name} {last_name}'
    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name,last_name)
    
    @classmethod
    def _validate(cls,name):
        if not name.isalpha():
            raise ValueError("Name must be alphabetical")
    
    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

        
# new_car = Car("honda", 2016, "Blue")

# new_car.start()
# new_car.paint("Yellow")
# new_car.accelerate
# new_car.stop()
# print(new_car.model)
# new_car.__class__model_year = 1500
# new_car.paint("blue")
# print(new_car.get_color())
# print(new_car.gas_mileage(1500,15))
