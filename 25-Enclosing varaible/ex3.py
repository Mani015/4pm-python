
a=10
def f2():
    a=20
    print(a)
    print(locals())
    locals()['a']=1;
    print(locals())
    print(globals()['a'])
    print(locals()['a'])
    def f1():
        print(locals()['a'])
    f1()
f2()