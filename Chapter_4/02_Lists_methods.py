friends = ["apple", "orange", "Aakash",5, 435., "Rohan", False]
friends.append("Arnav") # append is used to edit the list by adding new term after the last term/index
print(friends)

l1 = [1,34,56,62,6,11]
l1.sort() #.sort works with sorting numbers in asc order
print(l1)

l1.reverse() #.reverse will reverse the order of the og list l1 with no effect in sorting orderprint(l1) # prints the list from end index to 0th index

l1.insert(4,3333) # means insert 3333 such that its at index 3 now
print(l1)

l1.pop(4) #.pop removes the element of that index and returns the list without it
print(l1.pop(3)) # prints only the removed element of listprint(l1)

