from utils import value, fraction, printTable, diffPolynomial

#################################################################
##### USER DEFINED                                          #####
#################################################################

num = [ 1, -3, -10 ]

maxError = 0.000001

x1 = 7
x2 = 4

#################################################################
##### ITERATION                                             #####
#################################################################

dnum = diffPolynomial(num)

decimalPoint = '{0:.7f}'
data = [
    [str(0), decimalPoint.format(x1), '-'],
    [str(1), decimalPoint.format(x2), '-']
]
spaces = 13

def iterate(index):
    global x1, x2

    xnext = x2 - (x2 - x1) * value(x2, num) / (value(x2, num) - value(x1, num))
    error = abs(xnext - x2)

    x1 = x2
    x2 = xnext
    
    data.append([
        str(index),
        decimalPoint.format(x2),
        decimalPoint.format(error),
    ])

    if(error < maxError or xnext == 0): return True
    else: return False

for i in range(1, 100):
    status = iterate(i)
    if(status): break


headers = [
    'i',
    'CURRENT X',
    'CHANGE'
]
print('\nSECANT\n')
printTable(headers, data, spaces)

