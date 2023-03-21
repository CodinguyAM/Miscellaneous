def divisors(n):
    ds = []
    for d in range(n):
        if n % (d + 1) == 0:
                   ds.append(d+1)
    return ds

def allMultiplied(ls):
    p = 1
    for i in ls:
        p = p * i
    return p

def factorize(n):
    factors = []

    ##10s division check - improves efficency
    if str(n)[-1] == "0":
        #print(n, "ends with 0")
        divs = factorize(int(str(n)[:-1]))
        divs.extend([2, 5])

    ##exclude 1
    divs = divisors(n)[1:]

    ##its prime
    if divs == [1, n]:
        return [n]
    for div in divs:
        ##assume div is prime
        
        divIsPrime = True
        for div2 in divs:
            #print(div2, div, div % div2)
            if div % div2 == 0 and div != div2:
                ##divisor is not prime- div2 divides it
                divIsPrime = False
                break
        if divIsPrime:
            ## append only prime divs
            factors.append(div)
    #print(factors)
    if allMultiplied(factors) == n:
        ## do we have all factors
        return factors
    else:
        ## fix by adding the missing factors
        factors.extend(factorize( int( n/allMultiplied(factors) ) ) )
        return factors

while True:
    n = 20
    try:
        n = int(input("Enter number to factorize: "))
        print("Factorization of", n, "is", end=" ")
        fact = factorize(n)
        for f in fact[:-1]:
            print(f, end=" x ")
        print(fact[-1])
        print()
    except:
        print()
        print()
