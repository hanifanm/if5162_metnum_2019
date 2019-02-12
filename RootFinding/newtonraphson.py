from utils import value, fraction, printTable, diffPolynomial

#################################################################
##### USER DEFINED                                          #####
#################################################################

num = [ 1, -3, -10 ]

maxError = 0.000001

xnow = 7

#################################################################
##### ITERATION                                             #####
#################################################################

dnum = diffPolynomial(num)

decimalPoint = '{0:.7f}'
data = [[str(0), decimalPoint.format(xnow), '-']]
spaces = 13

def iterate(index):
    global xnow

    xnext = xnow - value(xnow, num) / value(xnow, dnum)
    error = xnext - xnow
    if(error < 0): error = -error

    xnow = xnext
    
    data.append([
        str(index),
        decimalPoint.format(xnow),
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
print('\nNEWTON RAPHSON\n')
printTable(headers, data, spaces)

