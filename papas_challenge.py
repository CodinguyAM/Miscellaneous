from math import *
##
##def maxPackageSize(n):
##    optimalSize = 0
##    OSR = 0
##    for I in range(1, n+1):
##        if n % I >= OSR:
##            optimalSize = I
##            OSR = n % optimalSize
##    return optimalSize
##
##while True:
##    PS = int(input("How many cupcakes has Chef baked?: "))
##    MPS = maxPackageSize(PS)
##    print("Optimal package size is", MPS, "cupcakes a package")
##    print("It leaves Chef", PS % MPS, "cupcakes")
##    print()
##
while True:
    PS = int(input("How many cupcakes has Chef baked?: "))
    MPS = floor(PS/2) + 1
    print("Optimal package size is", MPS, "cupcakes a package")
    print("It leaves Chef", PS % MPS, "cupcakes")
    print()
