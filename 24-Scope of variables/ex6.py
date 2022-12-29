# Enclosing variable:
a1=10
def func():
    def f1():
        a2 = 12
        print('global v:', a2)
    f1()


func()
print('global v:',a1)

