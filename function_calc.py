
import math
def func(cate, u_value):
    if cate==1:
        return math.sqrt(u_value)
    elif cate==2:
        return math.log(u_value)
    else:
        return math.sin(u_value)

cate= input("please select the calc type \n select 1 for sqrt of number \n select 2 for Natural logarithm (log base e) of the number \n  select 3 for Sine of the number (in radians) : ")
cate=int(cate)
u_value=int(input("please enter user value: "))
print(func(cate,u_value))