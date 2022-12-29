g1=100
print('global v:',g1)
def f1():
    g1=200
    print('enclosing varaible:',g1)
    print('global variable :',globals()['g1'])
    def f2():
        g1=300
        print('local v:',g1)
        print('global variable :', globals()['g1'])
    f2()
    print('global variable :', globals()['g1'])
f1()
print('global variable :', globals()['g1'])

# global v: 100
# enclosing varaible: 200
# global variable : 100
# local v: 300
# global variable : 100
# global variable : 100
# global variable : 100