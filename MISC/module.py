def myFunc():
    print("Hello world!")

myFunc()# prints the name of the file.py we using agar current me execute kara to current file naam warna import kara to imported file ka name print hoga
print(__name__) 

if __name__ == " __module_execution__":
    print("We are directly running this code")
    myFunc()
    print(__name__)