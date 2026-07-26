class Outer:

    def __init__(self):
        self.inner=Outer.Inner()
        self.inner.display()

    class Inner:
        def display(self):
            print("It is a Inner class Instance Method")


obj=Outer()