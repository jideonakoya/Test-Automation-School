class Hunt:
    __weapon = "Assault Rifle"

    def get_weapon(self):
        return self.__weapon + ":" + " Not Available"


hunt = Hunt()
print(hunt.get_weapon())
