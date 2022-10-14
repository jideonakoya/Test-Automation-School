
class Animal:

    group = "mammal"
    leg_count = 4

    # default constructor
    def __init__(self):
        self.name = "unknown"


class Vehicle:

    can_fly = False
    tire_count = 4

    # parameterized constructor
    def __init__(self, make):
        self.make = make

    def set_tire_count(self, count):
        self.tire_count = count

    def set_flyable(self, cfly):
        self.can_fly = cfly

    def get_make_tire_count(self):
        return self.make + ":" + str(self.tire_count)

    def check_type(self):
        if self.make == "Aeroplane":
            print("This is a plane")
        else:
            print("This is likely a car")


animal = Animal()
print("Animal:", animal.name, animal.group)

toyota = Vehicle("Toyota")
print("\nVehicle:", toyota.make, toyota.can_fly)
toyota.check_type()

lexus = Vehicle("Toyota")
print("\nVehicle:", lexus.make, lexus.can_fly)
lexus.check_type()

plane = Vehicle("Aeroplane")
plane.set_tire_count(3)
plane.set_flyable(True)
print("\nVehicle:", plane.make, plane.tire_count, plane.can_fly)
print(plane.get_make_tire_count())

plane.check_type()