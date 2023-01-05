g1=10
def outer():
    g1=20
    print('enclosing variable:',g1)
    def inner():
        nonlocal g1
        g1=30
        print('local v:',g1)
        def func():
            nonlocal g1
            g1=250
            print('lcoal v:',g1)
        func()
        print('enclosing v:',g1)
    inner()
    print('enclosing v:',g1)
outer()
print('global v:',g1)

# enclosing variable: 20
# local v: 30
# lcoal v: 250
# enclosing v: 30
# global v: 10


g1=10
def outer():
    g1=20
    print('enclosing variable:',g1)
    def inner():
        nonlocal g1
        g1=30
        print('local v:',g1)
        def func():
            nonlocal g1
            g1=250
            print('lcoal v:',g1)
        func()
        print('enclosing v:',g1)
    inner()
    print('enclosing v:',g1)
outer()
print('global v:',g1)





# enclosing variable: 20
# local v: 30
# lcoal v: 250
# enclosing v: 250
# enclosing v: 250
# global v: 10