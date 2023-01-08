class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return "Same point"
        else:
            return f"Distance between them is {abs(self.x-other.x)} in x and {abs(self.y-other.y)} in y"


point1=Point(1,2)
point2=Point(1,3)
print(point1==point2)