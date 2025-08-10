
class Vehicle:
    NUM_WHEELS = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    @classmethod
    def get_wheels(cls):
        return cls.NUM_WHEELS
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    pass



class Motorcycle(Vehicle):
    NUM_WHEELS = 2

class Truck(Vehicle):
    NUM_WHEELS = 6
    def __init__(self, make, model, payload):
        super().__init__(make,model)
        self.payload = payload


my_truck = Truck("Ford", "F-150", 1000)
print(my_truck.info())  # Ford F-150
print(my_truck.get_wheels())  # 6