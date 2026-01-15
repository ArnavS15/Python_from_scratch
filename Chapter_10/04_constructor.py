'''
class Employee: # a class is defined
    language = "Python" # these are class attributes
    salary = 1200000 

    def __init__(self):
        print("i am creating an object") # dunder methods me hai _init_ (starts and ends as _x_ ) and they get printed without getting called
        #init function me agar self ke aage aur attributes jode , use karke then we have to sepeartely define sabki self.values and then call then last me ek sath
    def getInfo(self): # class ke andar function daldia
        print(f"the language is {self.language}. the salary is {self.salary}")

    

harry = Employee() # init me defined attributes get called here likhna padta values me
# object = class call hote hi dunder methods get printed automatically
harry.name = "Harry"
print(harry.name, harry.salary) # ye print hua coz we did that
'''

class Employee:
    language = "Python"
    salary = 1200000

    def _init_(self, name, salary ,language ):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"the language is{self.language}. the salary is {self.salary}")

   
harry = Employee("Harry", 1300000 , "Javascript")
print(harry.name, harry.salary)