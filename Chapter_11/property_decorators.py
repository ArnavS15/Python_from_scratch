class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a a is {cls.a}")

    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self, value): # string is split such that ["Harry", "khan"] is a list of strings after the split at " " in which ie Harry is the 0th element and khan is the first string set as first name and last name respectfully]
        self.fname = value.split(" ")[0] # f for first name 
        self.lname = value.split("")[1] # l for last name
    
e = Employee()
e.a = 45
e.name = "Harry Khan"
print(e.name)
e.show()
