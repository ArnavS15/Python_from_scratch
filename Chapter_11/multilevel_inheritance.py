class Employee: # parent class is the base thus can execute only a info
    a = 1

class Programmer(Employee): # 1st level inheritance class will contain both 0th level and 1st level info
    b = 2

class Manager(Programmer): # 2nd level inheritance class will contain all three information levels
    c = 3

o = Employee()
print(o.a) # prints the a attribute
# print(o.b) # shows an error as there is no b attribute in employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)