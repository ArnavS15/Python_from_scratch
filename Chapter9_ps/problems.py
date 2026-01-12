# Q1 write a program to read the text from a given file "poems.txt" an find out whether it contains the word twinkle
with open("poems.txt") as f:
    content = f.read().lower()

if "twinkle" in content:
    print("twinkle is present")

else:
    print("twinkle is not present")

# Q2 the game() function in a program lets a user play a game and returns the score as an integer you need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score and write a program to update that whenever its broken by game() function
import random

def game():
    print("You ae playing the game...")
    score = random.randint(1,62) # score gets chosen randomly bw 1 and 62 everytime we run

    # fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""): # if hiscore is not! blank
            hiscore = int(hiscore) # that score becomes hiscore
        else:
            hiscore = 0

    print(f"your score: {score}")   
    if(score>hiscore): # is this happens then open file hiscore.txt and write the new hiscore there untill it gets beaten
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score # value is returned which is either less than hiscore or the new modified hiscore edited in the .txt file as well

game()    

# Q3 write a program to generate multiplication tables from 2 to 20 and write it to the different files.place these file in a folder for a 13 year old

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n"

    with open(f"tables/table_{n}", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)

# Q4 a file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ##### by updating the same file.
word = "donkey"
with open("donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("donkey.txt", "w") as f:
    f.write(contentNew)

# Q5 add a list of words to be added to the censored list in Q4
words = {"Donkey", "bad", "ganda"}
with open("donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("donkey.txt", "w") as f:
    f.write(content)
