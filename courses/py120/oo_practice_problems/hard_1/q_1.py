class RangeMixin:
    def range(self):
        if isinstance(self, Catamaran):
            return self.fuel_capacity * self.fuel_efficiency + 10
        return self.fuel_capacity * self.fuel_efficiency


class Vehicle(RangeMixin):
    def __init__(self, fuel_efficiency, fuel_capacity):
        self.fuel_efficiency = fuel_efficiency
        self.fuel_capacity = fuel_capacity


class Catamaran(Vehicle):
    def __init__(self, number_propellers, number_hulls, kilometers_per_liter, fuel_capacity):
        super().__init__(kilometers_per_liter, fuel_capacity)
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls

class WheeledVehicle(Vehicle):
    def __init__(self,
                  tire_list, fuel_efficiency, fuel_capacity):
        super().__init__(fuel_efficiency, fuel_capacity)
        self.tires = tire_list



    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)


auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0