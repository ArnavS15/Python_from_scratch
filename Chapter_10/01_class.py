# Object oriented programming yaha se start hogi 
# OOps
class Employee: # a class is defined
    name = "Harry"
    language = "Py"
    salary = 1200000 # these are class attributes
     

harry = Employee()
harry.name = "Harry Singh Chaddha" # this is an object/instance attribute
print(harry.name, harry.language)

rohan = Employee()
rohan.name = "Rohan Rogan Josh"
print(rohan.language,rohan.salary )

# name is object/instance attribute thus specific to each object individually
# salary and language are class attributes and belong to whole class universally

