a=int(input("Enyer a "))
b=int(input("Enter b "))
c=int(input("Enter c "))

d=(b*b)-4*a*c
root_d=d ** 0.5
if d>=0:
    root1=(-b+root_d)/4*a
    root2=(-b-root_d)/4*a
    print("First root : ",root1)
    print("Second root : ",root2)
else:
    print("Sorry there will be no root ")