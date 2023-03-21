from math import *

def do():
    limit = int(input("Limit?: "))
    funct = eval('lambda x: '+input("Booler?: "))
    for x in range(limit):
        if funct(x):
            print(x, "satisfies the equation.")
def rev(num):
    anum = int(abs(num))
    if anum == 0:
        return 0
    return int(str(anum)[::-1]) * num/anum

print(rev(-71))
while True:
    print()
    do()
