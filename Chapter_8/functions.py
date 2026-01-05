# suppose hume same set of codes repeat pe repeat karne hai
# jaise avg of 3 numbers to bar bar same lines of code likhne ki bajaye we can just define() those lines of code and then just type one line to replace and optimise lines of codes

# this is function definition

def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b +c)/3
    print(average)

avg() # this is function call
avg()
avg()
avg()

def goodDay():
    print("Good Day")
goodDay()


def goodDay(name, ending):
    print("Good Day!",name)
    print(ending)
    return "now BYE" # returns function with a value to the variable a here  
# return akele returns none to value of a at end
a = goodDay("Harry", "Thank You!")    
print(a) # printed with return me given value after a ka defined function runs pehle

def goodDay(name, ending="Thank you"): # ending define karne se this becomes DEFAULT ending
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry", "Thanks") # ending denge to yahi ayengi warna default
goodDay("Rohan")