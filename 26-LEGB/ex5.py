
# a=10
# print('global variable:',a)
# def f1():
#     a=20
#     print('locla varaible:',a)
# f1()
# print('global varaible:',a)
# global variable: 10
# locla varaible: 20
# global varaible: 10



a=10
print('global variable:',a)
def f1():
    global a
    a=20
    print('global varaible:',5+globals()['a'])
f1()
print('global varaible:',a-2)
# global variable: 10
# global varaible: python
# global varaible: python


