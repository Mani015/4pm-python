# How to accessing global varaible inside of function with the same
# Syntax: print(globals()['global variable name'])


G1=23
print('globa v:',G1)
# globa v: 23
def local():
    G1=20
    print('local v:',G1)
    # local v: 20
    print(G1)
#     20
    print('globa variable accessing the globals():',globals()['G1'])
#     globa variable accessing the globals(): 23


local()
