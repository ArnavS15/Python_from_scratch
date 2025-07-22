friends = ["apple", "orange", "Aakash",5, 435., "Rohan", False]
# Indexing: 0        1         2       3  4      5
print(friends[0])

#Lists are mutable therefore we can make changes in the og list
friends[0] = "Grapes"
print(friends)
print(friends[1:4]) #indexing principles of lists are exactly same as strings
# however when we made changes into strings it led to printing new strings with edits instead of modifying the og
# but its diff for lists

