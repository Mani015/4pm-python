# return may only occur syntactically nested in a function definition, not within a nested class definition.
# If an expression list is present, it is evaluated, else None is substituted.
# return leaves the current function call with the expression list (or None) as return value.
# When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function.
# In a generator function, the return statement indicates that the generator is done and will cause StopIteration to be raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the StopIteration.value attribute.
def additon(a,b):
    return a+b

# additon(10,20)
# 30
print(additon(10,20))