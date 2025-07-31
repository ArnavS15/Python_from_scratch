# Q1 write a python program to find remainder when a number is divided by z

a = 39
b = 5

print("Remainder when a is divided by b is ", a % b)
# % is modulo operator which gives remander for above)

# Q2 Write a program to check the type of variable assigned using input()function

a = input("Enter the value of a: ")
print(type(a))
# input type is always string but type conversion se change karte hai to our needed types

# Q3 Use comparision operator to find out whether a given variable is greater than b or not and take a = 34 and b = 80
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("value of a is greater than b : statement is ", a>b)

# Q4 Write a python program to find the average of 2 numbers entered by the user
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print("The Average of the 2 inputs is : ",(x+y)/2 )