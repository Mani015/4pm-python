# Global keyword:A global keyword is a keyword that allows a user to modify a variable outside the current scope.

# Use of global keyword in Python: To access a global variable inside a function, there is no need to use a global keyword

# without global keyword
# g1=100
# def func1():
#
#     g1=200
#     print('local v:',g1)
# func1()
# print('global v:',g1)

# local v: 200
# global v: 100


# using with global keyword

g1=100
def func1():
    global g1
    g1=200
    print('local v:',g1)
func1()
print('global v:',g1)
# local v: 200
# global v: 200