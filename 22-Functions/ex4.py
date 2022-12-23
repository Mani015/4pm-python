# 2).keywprd Arguments:

def keywordarguments(a1,b1,c1,d1):
    print(a1,
          b1,
          c1,
          d1)
    print(f'a1 value is {a1}-->'
          f'b1 value is {b1}-->'
          f'c1 value is {c1}-->'
          f'd1 value is {d1}')
# a1 value is 10-->b1 value is 20-->c1 value is 30-->d1 value is 40
# keywordarguments(a1=10,b1=20,c1=30,d1=40)
# 10 20 30 40


# keywordarguments(d1=40,a1=10,b1=20,c1=30)
# 10 20 30 40

a1=40
b1=30
c1=20
d1=10
keywordarguments(d1=10,b1=30,a1=40,c1=20)
# a1 value is 40-->b1 value is 30-->c1 value is 20-->d1 value is 10