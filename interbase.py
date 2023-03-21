def largestPowerLessThan(lim, b):
    e = 0
    while b ** e <= b:
        e = e + 1
    return e + 1

lplt = largestPowerLessThan
print(lplt(9, 2))


def convertTo(num, base, ):
    
