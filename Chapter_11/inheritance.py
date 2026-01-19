
class Employee: # ye base/parent class bangya and any change in this will be automatically synced to inheritance classes
    company = "ITC"
    def show(self):
        print(f"th name of employee is {self.name} and the salary is {self.salary} ")

'''
class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary} ")
    
    def showLanguage(self):
       
     print(f"the name is {self.name} and he is good with {self.language} language ")

# but this method is difficult to maintain balance of classes if 50 such were present kitna change karlete bhai
# thus we use inheritance
'''
class Programmer(Employee): # ye inheritance class hai
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language } language")
a = Employee()
b = Programmer()
print(a.company, b.company)


