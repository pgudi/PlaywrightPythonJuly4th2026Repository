class GeometricFigure:
    def area(self):
        print("Area of a Geometric Object!!")

class Square(GeometricFigure):
    def area(self):
        side=5
        result=(side * side)
        print("Area of a Square :",result)

class Rectangle(GeometricFigure):
    def area(self):
        length=10
        breadth=5
        result=(length * breadth)
        print("Area of a Rectangle :",result)

class Circle(GeometricFigure):
    def area(self):
        pi=3.14
        r=2.5
        result=(pi * r * r)
        print("Area of a Circle :",result)


figure=GeometricFigure()
figure.area()

sqaure=Square()
rect=Rectangle()
circle=Circle()

figure=sqaure
figure.area()

figure=rect
figure.area()

figure=circle
figure.area()

