import math
print("""
WELCOME TO COMPLEX NUMBER CALCULATOR
This program converts a rectangular coordinate system complex number to polar coordinate system complex number;
and vice- versa.
This is a free program and can be used and redistributed without any attribution.
""")
i = 0
while i == 0:
    c = input(" Please Enter the Coordinate System you want to convert : [R] for Rectangular, [P] for Polar or [Q] to quit the program: ")
    if (c.lower() == 'r'):
        a = int(input("Enter the Real Part (a) :"))
        b = int(input("Enter the imaginary Part (b) :"))
        print("YOU HAVE ENTERED Z = " , a , "+ i " , b)
        r = ((a*a) + (b*b))
        R = math.sqrt(r)
        angle = math.atan(b/a)
        print("Z in Polar Coordinate Format is : " , R , "\u2220 " , angle , "\u00b0")

    elif (c.lower() == 'p'):
        r = int(input("Enter the Magnitude(r) :"))
        theta = int(input("Enter the Angle Theta(\u03F4) :"))
        print("YOU HAVE ENTERED Z = ", r, "\u2220 ", theta , "\u00b0")
        u = r * math.cos(theta)
        v = r * math.sin(theta)
        print(" Z in Rectangular Coordinate Format is : " , u , " + i", v)
    elif (c.lower() == 'q'):
        print("THANK YOU AGAIN FOR USING THE PROGRAM ! GOOD BYE")
        break
    else:
        print("Enter Sensible Value")




