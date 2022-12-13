# 1.BREAK: break statement is one of the loop control statement use break control statement,
# when we want to exit the loop when certain condition is met
# t=(1,2,3,4,5,6,7,8,9)
#
# for l in t:
#     if l==5:
#         break
#     print(l)
# 1
# 2
# 3
# 4

# for i in range(0,20,2):
#     if i==14:
#         break
#     print(i)

for i in range(20):
    if i%2==0:
        if i==14:
            break
        print(i)
