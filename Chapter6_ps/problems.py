#Q1 write a program to find the greatest of 4 numbers entered by the user
a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1: " , a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a1: " , a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a1: " , a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a1: " , a4)

#Q2 write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass,assume 3 subjects and take marks as an input from the user

marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>33):
    print("You Passed to next grade:", total_percentage)

else:
    print("You failed, try again next year!:", total_percentage)

# Q3 A spam comment is defined as a text containing following keywords:
# "Make a lot of money" , "Buy Now" , "Subscribe this" , "Click this". Write a program to detect these spamms:
# p means phrase to look for
p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam") # case sensitive hai ye gadbad hai

else:
    print("This comment is not a spam")

#Q4 Write a program to find whether a given usernae contains less than 10 characters or not
username = input("Enter username:")
if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("All is well")


# Q5 write a program to find out if a given name is present in a list or not
l = ["Harry","Rohan","Shivya",'Rohan']
name =  input("Enter your name:")

if(name in l):
    print("Your name is in the list")
else:
    print('your name is not in the list')
# this is also case sensitive yaha pe names in list

