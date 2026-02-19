a = float (input("Enter side a: "))
b = float (input("enter side b: "))
c = float (input("enter side c: "))

s = ( a + b + c ) / 2
area = (s * (s - a ) * ( s - b ) * ( s - c )) ** 0.5

print ( "Area of triangle =" , area)