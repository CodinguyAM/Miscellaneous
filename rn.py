import random

def genndig(d):
    n = ""
    #repeat d times
    for f in range(d):
        n = n + str(random.randint(0, 9))
    return int(n)
print(genndig(int(input("Digits"))))
