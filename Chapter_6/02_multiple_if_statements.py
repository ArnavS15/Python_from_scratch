a = int(input("Enter your age"))

if(a%2 == 0):
    print("a is even") # if statement 1
# this if loop is different and thus works on its own and neeche wala apna alag loop hai

if(a>=18):
    print("You are above the age of concent")
    print("Good for you Homie!") # if statement 2
# thus as per outcome both if statements work independently but they do!

elif(a<0):
    print("You are entering and invalid age")

# agar hum yaha if lagate to codes 15,16,20 sab ek loop me ajate 
elif(a==0):
    print("O is not a valid age")


else:
    print("You are below the age of concent")
    print("oops! better luck next year.")


print("End of program")