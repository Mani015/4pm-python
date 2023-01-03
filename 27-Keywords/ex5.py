
a1=30
print('global v:',a1)
def func1():

    a1=20
    print('enclosing v:',a1)
    def func2():
        global a1
        a1=10
        print('local v:',a1)
    func2()
    print('enclosing v:',a1)
func1()
print('global v:',a1)

# global v: 30
# enclosing v: 20
# local v: 10
# enclosing v: 20
# global v: 10


a1=30
print('global v:',a1)
def func1():
    global a1
    a1=20
    print('enclosing v:',a1)
    def func2():
        global a1
        a1=10
        print('local v:',a1)
    func2()
    print('enclosing v:',a1)
func1()
print('global v:',a1)

# global v: 30
# enclosing v: 20
# local v: 10
# enclosing v: 10
# global v: 10