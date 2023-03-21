def show(ls):
    for E in ls:
        print(E)
def areless(ls,x):
    r = True
    for e in ls:
        if e < x:
            r = False
    return r


def fix(n):
    return int(n*100)/100
def isint(x):
    return float(int(x)) == x

def isDivisibleBy(x, y):
    #is x divisible by y
    return isint(x/y)

def findTwins(ls):
    twins = []
    for curEm in ls:
        for checkEm in ls:
            if checkEm == curEm + 2:
                twins.append((curEm, checkEm))
    return twins

def SieveOfEratosthenes(n, limit=0):
    crossedOut = []
    nums = range(1, n+1)
    primes = []
    for Num in nums:
        if Num in crossedOut or Num == 1:
            continue
        for check in nums:
            if isDivisibleBy(check, Num):
                crossedOut.append(check)
        primes.append(Num)
    P = primes
    for p in P:
        if p < limit:
            primes.remove(p)
        else:
            continue
    return primes

def maxTwin(ls):
    return max(findTwins(ls))

print("This is a Sieve of Eratosthenes program!")
while True:
    print("This program has three modes:")
    print("P mode, for printing the primes found")
    print("S mode, for printing some statistics")
    print("S+P mode for printing both! Also default")
    print()
    mode = input("Which mode would you like?: ")
    n = int(input("Upper bound: "))
    limit = int(input("Lower bound: "))
    if mode == "P":
        show(SieveOfEratosthenes(n, limit))
    elif mode == "S":
        primes = SieveOfEratosthenes(n, limit)
        print()
        print("Percentage of numbers in the specified range that were prime: Roughly", fix(len(primes)/(n-limit))*100)
        print("Number of twin primes:", len(findTwins(primes)))
        print("Percentage of primes that were also twins:", fix(len(findTwins(primes))/len(primes))*100)
        print("Largest twin prime pair:", maxTwin(primes)[0], maxTwin(primes)[1])
    else:
        primes = SieveOfEratosthenes(n, limit)
        show(primes)
        print()
        print("Percentage of numbers in the specified range that were prime: Roughly", fix(len(primes)/n)*100)
        print("Number of twin primes:", len(findTwins(primes)))
        print("Percentage of primes that were also twins:", fix(len(findTwins(primes))/len(primes))*100)
        print("Largest twin prime pair:", maxTwin(primes)[0], maxTwin(primes)[1])
