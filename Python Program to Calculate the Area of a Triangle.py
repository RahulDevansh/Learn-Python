#Python Program to Calculate the Area of a Triangle

side1=float(input("Enter side1 of triangle "))
side2=float(input("Enter side2 of triangle "))
side3=float(input("Enter side3 of triangle "))
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
print('The area of triangle : %0.2f' %area)
