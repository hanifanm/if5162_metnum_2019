import math
from utils import printTable

#################################################################
##### USER DEFINED                                          #####
#################################################################

# Real Function
def f(x):
    return math.cos(x)

# Range
x_range = [0, 3]

# X Approximate
x_app = 2.5

#################################################################
##### ITERATION                                             #####
#################################################################

def num2dec(num):
    return decimalPoint.format(num)

# Order
order = 3

data = []
data_formatted = []
decimalPoint = '{0:.7f}'
step = (x_range[1] - x_range[0]) / order

for i in range(order + 1):
    x_val = x_range[0] + i * step
    y_val = f(x_val)
    row = [i, x_val, y_val]
    for o in range(order): row.append(0)
    data.append(row)

for j in range(order):
    for i in range(order - j):
        col = 3 + j
        data[i][col] = (data[i+1][col-1] - data[i][col-1]) / (data[i + 1 + j][1] - data[i][1])

for row in data:
    data_formatted.append(map(num2dec, row))

headers = [
    'i',
    'X',
    'Y',
    'ST-1',
    'ST-2',
    'ST-3',
]
print('\nNEWTON\n')
printTable(headers, data_formatted)

result = 0
for j in range(order + 1):
    curr = data[0][2+j]
    for i in range(j):
        curr *= x_app - data[i][1]
    result += curr
print('Result : ', result)
