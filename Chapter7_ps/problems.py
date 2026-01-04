# Q1 using FOR LOOP, Write a program to print multiplication table of a given number using for loop
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i} ") #f use karna makes f string i.e variable inputs allowed

# isi me to print table in reverse order ie: 10 to 1 thus we replace i with (11-i) as 
'''
1 10 = 11
2 9 = 11
3 8 = 11
4 7 = 11
5 6 = 11
6 5 = 11
7 4 = 11
8 3 = 11
9 2 = 11
10 1 = 11
when added hence 11-i for reverse order me output
'''

# Q2 write a program to greet all person names stored in a list 'l' and which start with S
l = ["Harry", "Soham","Sundar","Sachin","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"hello {name}")

# Q3 do Q1 using WHILE LOOP : this helps interconversion bw for and while loops
n = int(input("Enter a number: "))
i = 1
while(i<11):
    print(f"{n} * {i} = {n * i} ")
    i +=1

# Q4 write a program to find whether given number is prime or not
n = int(input("Enter a number: "))

for i in range(2, n): # 2 se leke n-1 tak jayega count
    if(n%i) == 0:
        print(" Number is not prime")
        break
else:
    print("Number is prime")

# Q5 find the sum of first n natural numbers using while loop
n = int(input("Enter the number: "))
i = 1 # since natural numbers
sum = 0 # sum is initialised by 0 and prod. by 1
while(i<=n): # from 1 to n-1 wala but now with n
    sum += i # increment by i
    i+=1 # incremenet by 1
print(sum)

# Q6 find the factorial of a given number using for loop
n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1): # to actually get n instead of n-1
    product = product*i
print(f"the factorial of {n} is {product}")

# star pattern problems Q7,8,9
# for values of n=3 we start with 2 spaces from margin on the first single star

'''
   *
  ***
 ***** 

'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i)) # as we need 3-1 = 2 spaces
    print("*"* (2*i-1), end="") # end= blank used to stops the addition of blank spaces stars ke margin me and puts them along margin
# print("*"* i) this printed i = 1/2/3 me stars and we wanted odd series of stars:1/3/5

'''
for patterns of a ring/box
***
* *
***
'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    if(i==1 or i==n): # means start 1st and last row me gaps ni dene stars me
        print("*"*n, end="") 
    else:
        print("*", end="")
        print(" "* (n-2), end="") #this means space hogi between the first and last row of stars
        print("*", end="")
    print("")