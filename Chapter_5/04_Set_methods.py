s = {1,5,32,54,5,5,5,"Harry"}

# print(s,type(s))

s.add(566) # .add adds a new element at the end of set
print(s,type(s))

s.remove(1) # to remove an element and give the updated set
print(s)

s.pop() # removes a random element from the set and returns that

# read handbook/documentation

s1 = {1,45,6}
s2 = {7,8,1,78}

print(s1.union(s2))
print(s1.intersection(s2))
#self explanatory