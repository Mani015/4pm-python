
s1=10
def func1():
    global s1
    s1=20
    print('enclosing v:',s1)
    def func2():
        s1=30
        print('local varaible:',s1)
    func2()
    print('enclosing v:',s1)
func1()
print('global varaible:',s1)

# enclosing v: 20
# local varaible: 30
# enclosing v: 20
# global varaible: 20
