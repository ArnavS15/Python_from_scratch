# Dictionaries are different from lists and tuples as it relies on {key:value} mapping pairs to store data chunks
marks = {"Harry":100,
         "Shubham":56,
         "Rohan":72,
         0:"Harry"} # yes even this can be considered a pair
print(marks, type(marks)) # classs here is dict for dictionary

# here, indexing doesnt work for the values index but it does for keys
print(marks["Harry"]) # works and gives us value but
print(marks[100]) # isme key error ayega and this doesnt work

# Dictionaries are mutable and cannot contain duplicate keys!
#indexing is done very precisely to easily find specific key:value pair

