a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
d = float(input("Enter fourth number:"))
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if d > mx:
    mx = d
print("Maximum number is",mx)   