class User:
    __password = "password"

    def get_password(self):
        return self.__password


class ActiveUser(User):
    def get_password(self):
        return "******"


online_user = ActiveUser()
print(online_user.get_password())
