class Human:

    name = "Homosapiens"
    group = "Mammal"

    def get_name_and_group(self):
        return self.name + ":" + self.group


boy = Human()
print("Boy:", boy.name, boy.group)
girl = Human()
print("Girl:", girl.name, girl.group)
