import math
a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter third side: "))
s=((a+b+c)/2)
ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of Triangle= ",ar)
input()

