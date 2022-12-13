# Loop control or Repetative control statement
# based on the condition , the block of code will excute respectively.it control the flow of program
# TO create loop control statement we want  two keyword's
# 1.forloop:for loop is used to iterate the iterator (or) range iterator
#          (or)
# In Python, there is no C style for loop, i.e., for (i=0; i<n; i++).
# There is a “for in” loop which is similar to for each loop in other languages.
# Syntax:
# for iterator_var in sequence:
#     statements(s)



# Print 1st 50 even numbers using for loop

# for i in range(0,100,2):
#     print(i,end=',')

for i in range(100):
    if i%2==0:
        print(i,end=',')
# 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,