a = float(input("Enter first side (a):"))
b = float(input("Enter first side (b):"))
c = float(input("Enter first side (c):"))
S = (a + b + c)/2
area =(S*(S-a)*(S-b)*(S-c))**0.5
print("\nSemi-perimeter (S)=", S)
print("Area of the triangle =", area)