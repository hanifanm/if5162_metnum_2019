def value(x, polynom):
    result = 0
    current = 1
    for c in reversed(polynom):
        result += c * current
        current *= x
    return result

def fraction(x, num, denum):
    return value(x, num) / value(x, denum)

def diffPolynomial(polynom):
    result = []
    power = len(polynom) - 1
    for i, c in enumerate(polynom):
        result.append(c * power)
        power -= 1
    return result[:-1]

def diffFraction(num, denum):
    dnum = diffPolynomial(num)
    ddenum = diffPolynomial(denum)
    return (dnum, ddenum)

def printTable(headers, data, space=10):
    headerString = []
    for j, col in enumerate(headers):
        headerString.append(col.rjust(space))
    print('|| ' + ' | '.join(headerString) + ' ||')

    border = []
    for j, col in enumerate(headers):
        b = ''
        for i in range(space):
            b = b + '-'
        border.append(b)
    print('|| ' + ' | '.join(border) + ' ||')

    for i, row in enumerate(data):
        rowString = []
        for j, col in enumerate(row):
            rowString.append(col.rjust(space))
        print('|| ' + ' | '.join(rowString) + ' ||')