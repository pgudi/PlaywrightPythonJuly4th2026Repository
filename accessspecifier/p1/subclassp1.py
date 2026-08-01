from p1.protectionclass import Protection

class SubclassInP1Package(Protection):
    def __init__(self):
        super().__init__()
        print("Public Variable public_x:", self.public_x)
        print("Protected Variable _protected_y:", self._protected_y)
    #    print("Private Variable __private_z:", self.__private_z)
        print("--------------------------------------")
