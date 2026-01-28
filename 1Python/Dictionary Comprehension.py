dct = { str(i) : i for i in range(1,101)}
dctt = { 'num_' + str(i) : i for i in range(1,101)}
# to join num_ with i we concatenate it using + for string of num_ added to string (i)
print(dct)
print(dctt)

print("-" * 50)
# conditional dicts
dict = {'num_' + str(i) : i for i in range(1,11)}
dict = {k:v for k,v in dict.items() if v%3 == 0}
print(dict) 

print("-" * 50)
# condition here is to print for values which are divisible by 3 hence remainder = 0
# to filter out the above condition for the limited set of num_1 to num_10 ki range me items mein se 
# matrix ke sath
matrix = [[1,2,3], [4,5,6], [7,8,9]]
final_dct = {(i,j) : matrix[i][j] for i in range(3) for j in range(3)}
print(final_dct)