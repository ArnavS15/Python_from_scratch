# Q1 print twinkle twinkle little star poem in q command from the net
print('''twinkle twinkle little star,
How I wonder what you are;
All above the earth so high,
Like a diamond in the sky.''')

# Q2 powershell terminal access karke dekhlia ye wala python type karke
# Q3 ek module use karenge for python text to speech
import pyttsx3
engine = pyttsx3.init()
engine.say("this command speaks whatever the programmer asks of it inside these double colons")
engine.runAndWait()

#Q4 to list out all the files in a given path of a directory 
import os

# specify the directory you want to list
directory__path = '/'

# list all files and directories in the specified path
contents = os.listdir(directory__path)

# print each file and directory name
for item in contents:
    print(item)

