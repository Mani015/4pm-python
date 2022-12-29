# Scope of local variable:
# A user can only access a local variable inside the function but never outside it.

def Localvaraible():
    name='python'
    print('local varaible:',name)



Localvaraible()
print('local varaible :',name)
# NameError: name 'name' is not defined

