class Human:

    leg_count = 4
    can_walk = True

    def __init__(self, description):
        self.description = description

    def set_leg_count(self, count):
        self.leg_count = count


girl = Human("This is human")
print("Girl:", girl.description)

boy = Human("Young Man")
boy.set_leg_count(2)
print("\nHuman legs:", boy.leg_count)
