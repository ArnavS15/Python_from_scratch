#Q1 write a program to create a dictionary of Hindi words with values as their english translation and provide user with an option to look it up
words = {
    "madad": "Help",
    "kursi": "chair",
    "chai" : "Tea"
}

word = input("Enter Your Word: ")

print(words[word])

#Q2 Write a program to input 5 numbers from the user and display all the unique numbers once
s = set()

n = input("Enter number1: ")
s.add(int(n))

n = input("Enter number2: ")
s.add(int(n))

n = input("Enter number3: ")
s.add(int(n))

n = input("Enter number4: ")
s.add(int(n))

n = input("Enter number5: ")
s.add(int(n))

print(s)

#Q3 create an empty dictionary and allow 4 friends to enter their favourite language as value and use key as their names assuming unique names
d = {}
name = input("Enter friend name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter Language name: ")
d.update({name: lang})
print(d)

# if key is same by chance to usk jo value assign hogi even if duplicates then it would be assigned the final updated d.update value before printing
# if by chance values same ho then value same reh sakti hai dictionary me but key is unique because this is the identifier
# indexing doesnt work in sets
# a list can not be included in a set no matter the size of it
# because sets require immutable and hashable elements while lists are opposite of this
