#Q1 write a python program to display a user entered name followed by good afternoon using input(function)
name = input("Enter your name: ")
print(f"Good Afternoon {name} ")
# string se pehle f use karna makes it fstring taking string ke andar hi use{} to give input inside string

#Q2 Write a program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>" , "Arnav").replace("<|Date|>" , "24 September 2050"))
# this is called chaining of replacement (,) use karke

# Q3 Write a program, to detect double space in a string
name = "Harry is a good  boy  and"
print(name.find("  "))

name = "Harry is a good  boy  and"
print(name.find("good"))
# .find(" ") use karne se ye index inside " " find hota and if it doesnt exist to output is shown -1
# when we replace smthing with name.replace("x"," y") to orignal name string change ni hoti coz immutable hoti hai strings but we print a new replaced string!

