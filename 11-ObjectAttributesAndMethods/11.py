import math

class Figures():

    @staticmethod
    def circle(radius):
        x=(math.pi)*(radius**2)
        return x

    @staticmethod
    def rectangle(side1,side2):
        p=side1*side2
        return p

    @staticmethod
    def triangle(base,height):
        p=(base*height)/2
        return p


print(Figures.circle(3))
print(Figures.rectangle(4,7))
print(Figures.triangle(6,2))
