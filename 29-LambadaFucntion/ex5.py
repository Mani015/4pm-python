# MAP:
# syntax: map(functionname, iterable (or) sequence of values)
# iterable:list, tuple, set..............

t=(1,2,3,4,5,6,7,8,9)

def square(n):
    return n*n

x1=map(square,t)
# print(x1)
# <map object at 0x0000017E4FB58BB0>
# print(set(x1))
# {64, 1, 4, 36, 9, 16, 49, 81, 25}

print(tuple(x1))
# (1, 4, 9, 16, 25, 36, 49, 64, 81)
