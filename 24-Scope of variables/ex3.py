# global varaible:
# Variables that are created outside of a function  are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.



Global1=200
print('global variable:',Global1)
# global variable: 200
def Localvariable():
    Global = 100
    print('global variable:',Global1)
    # global variable: 200
    print('Local varible:',Global)
#     Local varible: 100

Localvariable()
