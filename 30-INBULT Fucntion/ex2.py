
# def oddnumber(k):
#     if k%2==1:
#         return k
# l1=[22,44,5,66,77,89,34,65,76,52]
# x=filter(oddnumber,l1)
# # x=filter(oddnumber,range(1,15))
# print(list(x))





z='abcdefghijklmnopqrstuvwxyz'

def consonanats(i):
    if i not in 'aeiou':
        return True
k=filter(consonanats,z)
# print(tuple(k))
# ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')














# filter in lambda function:

# print(tuple(filter(lambda n: n>=5,range(20))))
# (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)







print(list(filter(lambda n: n not in 'aeiou','abcdefghijklmnopqrstuvwxyz')))
# ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']






