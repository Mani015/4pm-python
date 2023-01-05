l=[1,33,44,11,22,55,67,89,34,25]

def f1(k):
    return k**3

z1=map(f1,l)
# print(list(z1))
# [1, 35937, 85184, 1331, 10648, 166375, 300763, 704969, 39304, 15625]




def Map_Square(a):
    return a**2

k=map(Map_Square,range(1,11))
# print(list(k))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(list(map(lambda i:i**2,range(10))))