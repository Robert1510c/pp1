x=int(input("Pierwsza współrzędna: "))
y=int(input("Druga współrzędna: "))

if x==0 and y==0:
    print("Point is located in the position (0,0)")
elif x>=0 and y>=0:
    print("Point is located in the first quadrant of the coordinate system")
elif x>=0 and y<=0:
    print("Point is located in the fourth quadrant of the coordinate system")
elif x<=0 and y>=0:
    print("Point is located in the second quadrant of the coordinate system")
elif x<=0 and y<=0:
    print("Point is located in the third quadrant of the coordinate system")
    