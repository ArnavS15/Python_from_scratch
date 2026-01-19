
class Employee: # ye base/parent class bangya and any change in this will be automatically synced to inheritance classes
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"th name of employee is {self.name} and the company is {self.company} ")

class coder:
    language = "Python"
    def printLanguages(self):
        print(f"out of all languages here, is your language: {self.language}")

class Programmer(Employee, coder): # programmer child class ko do parent classses dediye with coder being the 2nd parent class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language } language")
a = Employee()
b = Programmer()
b.show()
b.printLanguages()
b.showLanguage()


