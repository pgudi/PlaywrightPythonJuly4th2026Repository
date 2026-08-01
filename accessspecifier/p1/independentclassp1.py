from p1.protectionclass import Protection

class IndependentClassInP1Package:
    def __init__(self):
        o=Protection()
        print("Public Variable public_x:", o.public_x)
        print("Protected Variable _protected_y:", o._protected_y)
    #    print("Private Variable __private_z:", o.__private_z)
        print("--------------------------------------")

