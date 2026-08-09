class Protection:
    def __init__(self):
        self.public_x=100
        self._protected_y=200
        self.__private_z=300

        print("Public Variable public_x:",self.public_x)
        print("Protected Variable _protected_y:",self._protected_y)
        print("Private Variable __private_z:",self.__private_z)

        