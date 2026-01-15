class Employee: # a class is defined
    language = "Python" # these are class attributes
    salary = 1200000 
     

harry = Employee()
harry.language = "Javascript" # this is an object/instance attribute
print(harry.salary, harry.language)
# if we see yaha do languages hai but print ke time it sees if instance is given first to print it at top priority else it prints the info given to object 
# if we comment out given instance then object value hi print hogi
