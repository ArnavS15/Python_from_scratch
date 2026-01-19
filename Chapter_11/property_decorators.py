class Employee: # bhot line of code humne sirf class employee me bharke encapsulate kardia ie bhot units ko ek class me pack kardia
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property # property decorator me name is a function jo chalega but make it seem like its a property ki .name and return karke print karke hume firt name last name set karke miljaye thus abstraction ki user ko dikhega nhi the effort put in
    def name(self):
        return f"{self.fname} {self.lname}" # encapsulation me pata bhi ni chalega ki ek result ke lie kitna code backend pe hai

    @name.setter
    def name(self, value): # string is split such that ["Harry", "khan"] is a list of strings after the split at " " in which ie Harry is the 0th element and khan is the first string set as first name and last name respectfully]
        self.fname = value.split(" ")[0] # f for first name 
        self.lname = value.split(" ")[1] # l for last name
    
e = Employee()
e.a = 45
e.name = "Harry Khan"
print(e.fname, e.lname)
e.show()
