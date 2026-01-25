# sometimes code me agar error bhi aye to we dont want error to crash the program 
# we want ki error bhi print hoke display hi hojaye
# hence and try and exception are used for exception handling

try:
    a = int(input("Enter a number: "))
    print(a) # sahi value print hui ya enter ho payi to try karke kardo

except ValueError as v: # printed when we give input something that can not be converted to our needed datatype i.e if we give invalid data input type me
    print("Heyyyy")
    print(v)
    
except Exception as e: # multiple except statements can be used for different error handling in python
    print(e) # else error mat do aur error ko bhi print hi kardo taki crash na ho

else:
    print("I am Inside Else")
    # The else clause does NOT raise an exception.
    # It runs only when NO exception occurs.

finally: # can only be execute at the end of the program when its about to exit but print to hota hi hota hai mid programmes
    print("AB HOGYA CODE EXECUTE?")

print("Thank you!")