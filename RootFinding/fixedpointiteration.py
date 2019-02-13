from utils import value, fraction, printTable

#################################################################
##### USER DEFINED                                          #####
#################################################################

num = [ 3 ]
denum = [1, -2]

maxError = 0.000001

xnow = 4

#################################################################
##### ITERATION                                             #####
#################################################################

decimalPoint = '{0:.7f}'
data = [[str(0), decimalPoint.format(xnow), '-']]
spaces = 13

def iterate(index):
    global xnow

    fnow = fraction(xnow, num, denum)
    error = abs(fnow - xnow)

    xnow = fnow
    
    data.append([
        str(index),
        decimalPoint.format(xnow),
        decimalPoint.format(error),
    ])

    if(error < maxError or fnow == 0): return True
    else: return False

for i in range(1, 100):
    status = iterate(i)
    if(status): break


headers = [
    'i',
    'CURRENT X',
    'CHANGE'
]
print('\nFIXED POINT ITERATION\n')
printTable(headers, data, spaces)

