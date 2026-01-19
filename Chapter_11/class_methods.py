class Employee:
    a = 1
    def show(self): # self likhne se instance attribute print hoga i.e e.a = 45 print hoga
        print(f"the class attribute value of a is {self.a}")

e = Employee()
e.a = 45
e.show()

# but if we want to print class attribute we have to use decorator @classmethod thus class access hoga with cls instead of self value
# staticmethod is also a decorator

class Employee:
    a = 1
    @classmethod
    def show(cls): # cls likhne se cls attribute print hoga i.e e.a = 1 print hoga
        print(f"the class attribute value of a is {cls.a}")

e = Employee()
e.a = 45
e.show()