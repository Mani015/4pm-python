l=[1,2,3,4,5,6,7]
print(l)
# [1, 2, 3, 4, 5, 6, 7]
# print(type(l))
# List append method  it adding single data from end of the list,it has taken only one argument
l.append(12)
print(l)
# [1, 2, 3, 4, 5, 6, 7, 12]

l.append(13)
print(l)
# [1, 2, 3, 4, 5, 6, 7, 12, 13]


l.append(14,15)
print(l)
# TypeError: list.append() takes exactly one argument (2 given)
