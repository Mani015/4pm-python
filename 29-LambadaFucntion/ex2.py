# lambda function is a single line function

# Syntax:lambda arguments : expression

# (lambda a,b:print(a+b))(10,20)
# 30

n1=int(input('Enter one number:'))
n2=int(input('enter second number:'))
(lambda a,b:print(a-b))(n1,n2)
(lambda a,b:print(a*b))(n1,n2)
(lambda a,b:print(a/b))(n1,n2)
# 10
# 200
# 2.0