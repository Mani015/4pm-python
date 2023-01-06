
# REDUCE:
# syntax: reduce (functionname, iterable)


from functools import reduce

def addtion(x,y):
    return x+y



r=reduce(addtion,[1,2,3,4,5,6])
# print(r)
# 21


def multiplication(a,b):
    return a*b

k=reduce(multiplication,range(1,7))
# print(k)
# 720


print(reduce(lambda x,y:x+y,[22,33,44,1,5,6,7]))
# 118


