

s={1,2,3,4,5,6}
print('before :',s)
def func():
    s.update({7,8})
    print('update:',s)
func()
# before : {1, 2, 3, 4, 5, 6}
# update: {1, 2, 3, 4, 5, 6, 7, 8}

