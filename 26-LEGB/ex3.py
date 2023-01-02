# Global scope:

z1=10
print('globa variable:',z1)
def func1():
    # z1=100
    # print('non local varaible:',z1)
    def func2():
        z2=200
        # print('local varaible:',z2)
    func2()
func1()
print('global variable:',z1)


# globa variable: 10
# global variable: 10