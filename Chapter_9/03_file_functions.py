f = open("coded_file.txt")

#lines = f.readlines() # readlines can be run multiple times to read multiple lines but gives empty string that if when all lines get finished thus this process works best in while loop
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

f.close()

# shortcut to this
'''
line = f.readline()
while(line != ""):
      print(line)
      line = f.readline
f.close()
'''
