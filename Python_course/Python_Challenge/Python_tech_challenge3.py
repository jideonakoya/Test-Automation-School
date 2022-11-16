# Using the OOP feature Inheritance, create a class Animal with the method sound() and then create a
# Cat and Dog class that inherits from the Animal class. The Cat and Dog class should override the sound class and
# print a different sound


class Animal:
    def sound(self):
        ani_sound = "Moo"
        return ani_sound


class Pigeon(Animal):
    def sound(self):
        ani_sound = "Coo"
        return ani_sound


class Wolf(Animal):
    def sound(self):
        ani_sound = "Howl"
        return ani_sound


pigeon_sound = Pigeon()
wolf_sound = Wolf()
print("Pigeon says: ", pigeon_sound.sound())
print("Wolf says: ", wolf_sound.sound())



