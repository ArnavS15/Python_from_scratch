marks = {"Harry":100,
         "Shubham":56,
         "Rohan":72,
         0:"Harry"}

print(marks.items()) # prints all items of dictionaries as a ('list') of key:value pairs as elements in a [tuple]

print(marks.keys()) # prints only the keys of the tuple
print(marks.values()) # prints only the values of the tuple

marks.update({"Harry": 99}) # will update the orignal dictionary with the new value to the used key as 
print(marks) # as after every update we will have to print alagse as dicts are mutable
# ({"key : New value"})

marks.update({"Saksham":0}) # we can also add new data pairs which will be appended to last of the tuple
print(marks)

print(marks.get("Harry")) # .get prints none if we use wrong key
print(marks["Harry"]) # prints error if we use wrong key due to [sq brackets]
# refer python dictionary methods from handbook or gpt
# pop method 
# pop item method
