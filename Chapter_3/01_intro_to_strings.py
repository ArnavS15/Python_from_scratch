name = "Harry"
#index: 01234 therefore 5 indexes or characters present    

nameshort = name[0:3] # [starting index : end index] form, where end is not included
# eg: here we start from 0 index all the way till 3 (0 1 2 thus excludes 3rd index)
print(nameshort) 
character1 = name[4]
print(character1)

print(name[0:3])
print(name[-4: -1]) 
# end se counting starts with negative therefore positive me karlo
print(name[1:4])

print(name[:4]) # is same as print(name[0:4]) from start index if lhs of : is empty
print(name[1:]) # is same as print(name[1: length]) or print(name[1:5])
print(name[1:5])