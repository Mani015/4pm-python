
x1=12
print('global v:',x1)
def func1():
    global x1
    x2=13
    # print('enclosing v:',x2)
    def func2():
        global x1
        x1=30
        # print('local v:',x1)
    func2()
func1()
print('global v:',x1)

# global v: 12
# global v: 30
