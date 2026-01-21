# Q1 create a class (2D vector) and use it to create another class representing a 3D vector
class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j ")



class ThreeDvector(TwoDvector): # 3d vector has to be inherited from 2s vector
    def __init__(self, i, j, k):
        super(). __init__(i,j) # self.i and self.j call hojayenge apne aap
        self.k = k # sirf k ko set kara coz uper constructor ko call karke i j apne aap call hojaeynge
   
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k ")

a = TwoDvector(3,7)
a.show()
b = ThreeDvector(1,2,3)
b.show()

# Q2 create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!!")

d = Dog
d.bark() # variable = class mention karte hai to call from that classs
# variable.defined function() karke call hota hai whatever we wanted to print in mentioned class

# Q3 Create a class "Employee" and add salary and increment properties to it
# cont: write a method 'SalaryAfterIncrement' with @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    pass
    salary = 2340
    increment = 20 # humne ise class me dalke class attribute banadia warna e.salary and e.increment likhke object attribute bhi bana sakte the neeche object ke
    @property # this decorator returns anything we want
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = (((salary/self.salary) -1)*100)


e = Employee() # employee class ka object banadiya
#print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2808
print(e.increment)


# Q4 Write a class 'complex' to represent complex numbers along with overloaded operators "+" and "*" which adds and multiplies them
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i) 
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i *c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i" # after addition to return the outcome as real and imaginary part seperate
    
c1 = Complex(1,2)
c2 = Complex(3,5)
print(c1 + c2)
print(c1*c2)
 # but for complex objects with real(r) and imaginary parts(i) this operand doesnt work here

# Q5 write a class vector representing a vector of n dimensions. overload the + and * operator which calculates the sum and the dot(.) product of them
class Vector:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z

def __add__(self,other):
    result = Vector(self.x + other.x, self.y + other.y, self.z + other.z )
    return result

def __mul__(self, other):
    result = self.x * other.x + self.y * other.y + self.z * other.z
    return result

def __str__(self):
    return f"Vector({self.x}, {self.y}, {self.z})"

# Test the imple