l1=[1,2,3,4,5,34,57,89,23,43]
# if l1%2==1:
    # print(l1)
# TypeError: unsupported operand type(s) for %: 'list' and 'int'

# Using for loop

# for k in l1:
#     if k%2==1:
#         print(k)



for k in l1:
    k=k+1
    print(k,end=',')

# 2,3,4,5,6,35,58,90,24,44,
