# Enclosing fnction:

# z1=10
# def func1():
#     # z1=100
#     print('non local varaible:',z1)
#     def func2():
#         z2=200
#         # print('local varaible:',z2)
#     func2()
# func1()

# non local varaible: 100


# enclosing varaible accesing the global scope:
z1=10
def func1():
    # z1=100
    print('non local varaible:',z1)
    def func2():
        z2=200
        # print('local varaible:',z2)
    func2()
func1()
# non local varaible: 10