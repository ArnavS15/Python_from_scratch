class person: # class ke andar attributes define karre
    name = "Arnav"
    problem = "Riddhima"

p1 = person() # this is object ya instance attribute jo call horhe using class
print(p1.name)
print(p1.problem)

# now to adjust and set new values ie set a new object in the same class
p1.name = "Aru"
p1.problem = "Khushu"
print(p1.name)
print(p1.problem)

# same we can do by setting p2 = person()
# ab new attributes for a new object but in the same class can be set and called
