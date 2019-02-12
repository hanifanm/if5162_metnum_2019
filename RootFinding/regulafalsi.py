from utils import value, fraction, printTable

#################################################################
##### USER DEFINED                                          #####
#################################################################

num = [ 1, -3, -10 ]
denum = [1]

maxError = 0.000001

xhi = 7
xlow = 2.5

#################################################################
##### ITERATION                                             #####
#################################################################

data = []
decimalPoint = '{0:.7f}'
spaces = 13

def iterate():
    global xhi
    global xlow

    fhi = fraction(xhi, num, denum)
    flow = fraction(xlow, num, denum)

    xmid = xhi - fhi * ( xhi - xlow ) / (fhi - flow)
    fmid = fraction(xmid, num, denum)

    dirc = ''

    if(fhi * fmid < 0):
        error = xmid - xlow
        newxhi = xhi
        newxlow = xmid
        dirc = '>>'
    else:
        error = xhi - xmid
        newxhi = xmid
        newxlow = xlow
        dirc = '<<'
    
    data.append([
        decimalPoint.format(xlow),
        decimalPoint.format(xmid),
        decimalPoint.format(xhi),
        decimalPoint.format(flow),
        decimalPoint.format(fmid),
        decimalPoint.format(fhi),
        dirc,
        decimalPoint.format(error)
    ])

    xhi = newxhi
    xlow = newxlow

    if(error < maxError or fmid == 0): return True
    else: return False

for i in range(100):
    status = iterate()
    if(status): break


headers = [
    'X LOW',
    'X NEW',
    'X HIGH',
    'Fx LOW',
    'Fx NEW',
    'Fx HIGH',
    'DIRECTION',
    'CHANGE'
]
print('\nREGULA FALSI\n')
printTable(headers, data, spaces)

