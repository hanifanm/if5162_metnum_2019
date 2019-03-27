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

for i in range(n):
    x_val = x_range[0] + i * step
    y_val = f(x_val + step / 2)
    result += y_val

result = result * step

print('Result : ', result)
