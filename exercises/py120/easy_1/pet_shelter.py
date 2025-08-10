class Pet:
    def __init__(self, type_of_pet, name):
        self.type_of_pet = type_of_pet
        self.name = name

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
    def number_of_pets(self):
        return len(self.pets)
    

class Shelter:
    def __init__(self):
        self.adoptions = {}
        self.shelter_animals = []
    
    def adopt(self, owner, pet):

        if pet in self.shelter_animals:
            owner.pets.append(pet)
            if owner.name in self.adoptions:
                self.adoptions[owner.name].append(pet)
                self.shelter_animals.remove(pet)
            else:
                self.adoptions[owner.name] = [pet]
                self.shelter_animals.remove(pet)
        else:
            print(f"{pet.name} is not available for adoption.")
    def add_animal(self,pet):
        self.shelter_animals.append(pet)

    def print_total_pets(self):
        print(f"The Animal Shelter has the following unadopted pets:")
        for pet in self.shelter_animals:
            print(f"a {pet.type_of_pet} named {pet.name}")
        
        for owner, value in self.adoptions.items():
            print(f"{owner} has adopted the following pets:")
            for pet in value:
                print(f"a {pet.type_of_pet} named {pet.name}")
            print('\n')
        
        print(f"The animal shelter has a total of {len(self.shelter_animals)} unadopted pets.")
    

    
cocoa = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.add_animal(cocoa)
shelter.add_animal(cheddar)
shelter.add_animal(darwin)
shelter.add_animal(kennedy)
shelter.add_animal(sweetie)
shelter.add_animal(molly)
shelter.add_animal(chester)
shelter.add_animal(Pet('dog', 'Rex'))
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_total_pets()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")