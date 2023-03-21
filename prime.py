from math import *
from random import *

def divisors(n):
    ds = []
    for d in range(n):
        if n % (d + 1) == 0:
                   ds.append(d+1)
    return ds

#print(divisors(200))

def GCD(a, b):
    ads = divisors(a)
    bds = divisors(b)
    cds = []
    for ad in ads:
        for bd in bds:
            if ad == bd:
                cds.append(ad)
    return max(cds)

#print(GCD(210, 312))

def isPrime(n, tests=1000):
    prime = True
    for I in range(tests):
        if not prime:
            return False
        a = floor(uniform(2, n))
        if GCD(a, n) == 1:
            prime = (a ** (n - 1)) % n == 1
            #print(a ** (n-1) % n)
        else:
            #print("Nopes, its divisible by", a)
            prime = False
    return prime
while True:
    print()
    n = int(input("Hi! What's your number?: "))
    if n < 1000:
        if isPrime(n):
            print("It's prime")
        else:
            print("It's composite, and its divisors are: ")
            for e in divisors(n)[:-1]:
                print(e, end=", ")
            print("and", divisors(n)[-1])
    else:
        if isPrime(n, ceil(n/2)):
            print("It's prime")
        else:
            print("It's composite, and its divisors are: ")
            for e in divisors(n)[:-1]:
                print(e, end=", ")
            print("and", divisors(n)[-1])
