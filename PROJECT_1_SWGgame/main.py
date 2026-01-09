import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1]) # random does well what its supposed to from the ([choices])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w" : -1, "g": 0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}
you = youDict[youstr]

print(f"you chose {dict[you]}\ncomputer chose {reverseDict[computer]}")
if(computer ==you):
    print("its a draw")

# Nested Loop ka example ek if else ke andar dusra if else
else: 
    if(computer ==-1 and you ==1): # snake drinks computer-water
        print("you Win!")

    elif(computer ==-1 and you ==0): # gun gets destroyed by water
        print("you lose...")

    elif(computer ==1 and you ==-1): # computer-snake drinks water ulta
        print("you lose...")

    elif(computer ==1 and you==0): # gun kills snake
        print("you Win!")

    elif(computer ==0 and you==1): # snake gets killed by gun
        print("you lose...")

    elif(computer ==0 and you==-1): # water destroys gun
        print("you Win!")

    else:
        print("something went wrong!")
''''''

# if i have to make multiple roudns to while loop chalana padega

if (computer - you) in [2, -1]:
    print("You win!")
elif computer == you:
    print("Its a draw")
else:
    print("You lose!")

# SHORTCUT HERE

