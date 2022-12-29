# Global Scope:
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

a=10
print('globa variable:',a)
# globa variable: 10
def f1():
    a1=20
    print(a1)
    print(a1)
    print(a1)
    print('globa varaible:',a)
    print('locla varaible:',a1)
#     locla varaible: 20

f1()
print('global varaible:',a)
# global varaible: 10
# print('locla v:',a1)
# NameError: name 'a1' is not defined