# Local scope:

# g1=10
# def outer():
#     x1=20
#     # print('enclosing variable:',x1)
#     def inner():
#         z1=30
#         print('local variable:',z1)
#     inner()
# outer()
# local variable: 30



x1=10
def outer():

    # print('enclosing variable:',x1)
    def inner():

        print('local variable:',x1)
    inner()
outer()
# local variable: 20










