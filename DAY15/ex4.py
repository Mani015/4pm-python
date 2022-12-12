
# Nested if:

n1=int(input('enter one input:'))
if n1>10:
    print('n1 is grater than 10')
    if n1>10:
        print('n1 is greater than 10')
    else:
        print('n1 is less than 10')
else:
    print('n1 is less than 10')