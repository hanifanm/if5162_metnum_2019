import math

#################################################################
##### USER DEFINED                                          #####
#################################################################

# Real Function
def f(x):
    return math.cos(x)

# Range
x_range = [0, 1.2]

# Order
order = 3

# X Approximate
x_app = 0.5

#################################################################
##### ITERATION                                             #####
#################################################################

result = 0
step = (x_range[1] - x_range[0]) / order

for i in range(order + 1):
    x_val = x_range[0] + i * step
    y_val = f(x_val)
    num = 1
    denum = 1
    for j in range(order + 1):
        if(i==j): continue
        x_now = x_range[0] + j * step
        num *= x_app - x_now
        denum *= x_val - x_now
    result += y_val * num / denum

print('Result : ', result)