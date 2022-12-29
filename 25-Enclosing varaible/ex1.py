# Enclosing Variable:

x1=15
print('global variable:',x1)
def outerfunction():
    a=20
    print('enclosing v:',a)
    def innerfuction():
        x1=20
        print('local variable:',x1)
    innerfuction()
outerfunction()
print('global variable:',x1)

# global variable: 15
# enclosing v: 20
# local variable: 20
# global variable: 15