# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def fun_one(n):
    if fun_three(n) % 2 == 0:
        answer = 1
    else:
        answer = n
    return answer

def fun_two(n):
    if n < 20:
        answer = fun_one(n)
    else:
        answer = 10
    return answer

def fun_three(n):
    answer = fun_two(2*n)
    return answer

print(fun_two(4))

"""
Note this must terminate because we can calculate (in finite time) fun_two(n)
if we can calculate fun_one(n), which can be done if we can find find_three(n),
which can be done if we can find fun_two(2*n). Therefore the input into
fun_two keeps getting larger, so eventually is larger than 20. At this point
we know the function outputs 10 and our chain terminates.
"""