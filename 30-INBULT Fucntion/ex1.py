# Filter()
# syntax:filter(functioname, iterable)
def Func(x):
    if x%2==0:
        return x
l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
x1=filter(Func,l)
print(x1)
# <filter object at 0x000001DBAFB45FA0>

print(tuple(x1))
# 2, 4, 6, 8, 10, 12)

