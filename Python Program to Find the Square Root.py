#Python Program to Find the Square Root
import cmath
 
# for integer and positive number
num = float(input("Enter a number"))
print("The squre root : ",num ** 0.5 )

# for real number and and negative number
num_c=eval(input("Enter a number"))
print("The squre root : ",cmath.sqrt(num_c))
