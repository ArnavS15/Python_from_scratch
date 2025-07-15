a = 31
t = type(a) # class <int>

print(t)

b = "Harry"
u = type(b) # class str

print(u)

c = "31.2"
d = float(c) # c but the type should be float
# v = type(c)
v = type(d)

print(v)
# type agar c ka nikalenge jo given value thi to uska orignal hi ayega data type but new variable ko use karenge type ke andar to final converted hi ayega!