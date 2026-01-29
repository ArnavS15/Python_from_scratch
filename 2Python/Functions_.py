def greet():
    print('Hello')

print([i for i in range(1,10)]) # gives values 1 to 10 in a list
print([greet() for i in range(1,10)]) # yaha func call karne se for loop call karke 
# hello gets printed 10 times 
# but none gets printed 20 times in list why:
# becoz something we get with return called compulsarily with a function
# we didnt return anything hence none got called that number of times

g_var = 10
def scope():
    l_var = 5
    print(g_var, l_var)
scope() # only this gets printed coz iski details are inside defined function

# Passing the paramters in a func.
def greet(n):
    print("Hell yeah", n)

greet("AKHILESH")

# method 2
def greet(name = '-----'):
    print("Hell yeah", name)

greet(name = 'AKHILESH')

# example
def subm(a = 0, b = 0):
    print(a,b,a+b)
subm(5,10)

subm(a = 5, b = 10)
subm(5) # if we give one value so it assumes it to be the first a ki value and assumes the rest to be 0
subm(b =5)
subm() # 0 hi ayengi teeno values

# using return
def arithmetic(a = 0, b = 0):
    return a + b, a-b, a*b

s = arithmetic(5,10) # sirf values define kardi instead of printing values bar bar
print(type(s)) # tuple hai ye
print(s)

# calling different functions

lst = [1,4,7,10] # sq brackets used yaha

def sq(lst): # curved brackets
    return[i**2 for i in lst] # sq brakcets used

def cu(lst):
    return[i**3 for i in lst] 

def final(lst):
    lst_1 = sq(lst)
    lst_2 = cu(lst)
    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]

print(final(lst))
print(sq((lst)))
print(cu((lst)))
