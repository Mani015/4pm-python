
# reduce(functionname, iterable)
# from functools import reduce

# print(reduce(lambda x,y:x+y,list(filter(lambda n:n>20,map(lambda i:i**2,range(1,15))))))


Telugu=int(input('Enter telugu score:'))
maths=int(input('Enter maths score:'))
physics=int(input('Enter physics score:'))
chemistry=int(input('Enter chemistry score:'))
biology=int(input('Enter biology score:'))

Total= Telugu+maths+physics+chemistry+biology
print('Total score:',Total)
print()
percentage=(Total/500)*100
print()
print('percentage of bastment:',percentage)





