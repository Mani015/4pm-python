# Nested list
l=[1,2,3,[1,2,3,[5,6,[4,2,3],22,10,45],56,'value'],'python',[12,13,14,[10,20],45],1,20,30]
# print(l)
# [1, 2, 3, [1, 2, 3, [5, 6, [4, 2, 3], 22, 10, 45], 56, 'value'], 'python', [12, 13, 14, [10, 20], 45], 1, 20, 30]
# print(l[0])
# 1
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])
# print(len(l))
# print(l[2])
# 3
# print(l[3])
# [1, 2, 3, [5, 6, [4, 2, 3], 22, 10, 45], 56, 'value']
# print(l[3][4])
# 56
# print(l[3][3])
# [5, 6, [4, 2, 3], 22, 10, 45]

# print(l[3][3][2])
# [4, 2, 3]

# print(l[3][3][2][4])
# IndexError: list index out of range
print(l[3][3][2][2])
# 3
print(l[3][3][2][-1])
# 3

