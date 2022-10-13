class Human:
    leg_count = 4
    gender = "Unknown"

    def get_gender(self):
        print("Gender: {", self.gender + " }")


class Man(Human):

    def __init__(self, gender):
        self.gender = gender


class Woman(Human):

    def __init__(self, gender):
        self.gender = gender


gender1 = Human()
gender1.get_gender()

man1 = Man("Male")
man1.get_gender()

woman1 = Woman("Female")
woman1.get_gender()
