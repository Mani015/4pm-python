# Variable length Arguments:
# 1).variable lenght
# 2).keyword  variable lenth arguments
# Variable-length arguments, abbreviated as varargs,
# are defined as arguments that can also accept an unlimited amount of data as input.
# The developer doesn't have to wrap the data in a list or any other sequence while using them.

def func(*teja):
    print(teja)

# func()
# ()

func(1,2,3,4,5)
# (1, 2, 3, 4, 5)


