import abc


class Vehicle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drive_direction(self):
        pass


class Car(Vehicle):

    def drive_direction(self):
        return "Drive Forward"


class Plane(Vehicle):

    def drive_direction(self):
        return "Drive Upward"


car1 = Car()
print(car1.drive_direction())

plane1 = Plane()
print(plane1.drive_direction())





