'''
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
'''
'''
# Q6 write a program to mine a log file and find out whether it contains 'python'
with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("yes python is present")
    
else:
    print("python is not present")

# Q7 find the line number which has python word from the log file
with open("log.txt") as f:
    lines = f.readlines() # content changes to line # means to check content line by line we use readlines and lines instead of read and content for f. respectively!

lineno = 1 # to start the checking from first line of the file content
for line in lines:
    if("python" in line.lower()):
        print(f"yes python is present, line no:{lineno}")
        lineno += 1 # because this was all for line 1 and we want all lines to be checked islie like a loop humne end me increment daldia for the check loop to cover through all lines one by one
'''
'''        
# Q8 write a program to make copy of a text file "this.txt"
with open("this.txt") as f:
    content = f.read() # ek file banake content dala usme orignal hogya jo

with open("this_copy.txt", "w") as f: # write ke bharose ek nayi file banegi copy file " " and uska content since write me hora wo bhi content means what was defined in orignal file wala codes
    f.write(content)
    f.write("\nsee we did copy all the lines of og content") # the line of code we can use to copy all the lines from og and add another wanted line to our new file without disturbing the orignal file
    # \n used dekhlena "string" me .write ke aage
'''
'''
# Q9 write a program to check if two files are identical
with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt")as f:
    content2 = (f.read)

if (content1 == content2):
    print("yes files are identical")
else:
    print("no they are not identical")
'''
# Q10 write a program to wipe the content of a file
with open("file.txt", "w") as f:
    f.write("") # blank write kardo to wipe out hojayega

# Q11 write a python program to rename a file to "renamed_by_python.txt" 
with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt" , 'w') as f:
    f.write(content) # content likhdia yaha pe to means ki link kardia 2 ko and use hi modify kara hai through write