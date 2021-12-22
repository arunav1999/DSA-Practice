import copy
# Concept of Shallow Copy and Deep Copy

#Deep copy
ls = [1,2]
temp = copy.deepcopy(ls)
temp[0] = 2
print(temp)
print(ls)

#Shallow copy

ls = [1,2]
temp = ls 
temp[0] = 2
print(temp)
print(ls)
