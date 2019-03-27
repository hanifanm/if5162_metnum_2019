import math

#################################################################
##### USER DEFINED                                          #####
#################################################################

def f(x):
    return math.exp(x)

x_range = [1.8, 3.4]
n = 8
step = 0.2

#################################################################
##### ITERATION                                             #####
#################################################################

result = 0

for i in range(n + 1):
    c = 1
    if(i==0 or i==n): c = 1
    elif (i%3==0): c = 3
    else: c = 2
    x_val = x_range[0] + i * step
    y_val = f(x_val)
    result += c * y_val

result = result * step * 3 / 8

print('Result : ', result)
