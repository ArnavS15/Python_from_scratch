class Employee: # a class is defined
    language = "Python" # these are class attributes
    salary = 1200000 
    def getInfo(self): # class ke andar function daldia
        print(f"the language is {self.language}. the salary is {self.salary}")

    '''
    def greet(self):
        print("Good Morning") # if we dont want to use self here we can independently print this for the whole class using
        # @staticmethod 

    '''

    @staticmethod # this decorater negates the need of object and its attributes
    def greet():
        print("Good Morning")
    

harry = Employee()
harry.language = "Javascript" # this is an object/instance attribute
harry.getInfo()
harry.greet()
 # harry is an object of employee class but error ayega ise chalane me
# the above call gets converted to Employee.getInfo(harry)
# but for this to actually run we have to specify the obeject as self in brackets taki us partivular object ki detailss print ho
# yaha harry. lagate to pass that object def function me
# if we dont use self yaha pe and khali harry.getInfo() use karte
# to error ata coz info define hi sirf employee class ki kar rakhi not harry object ki usla sirf ek language defined tha
