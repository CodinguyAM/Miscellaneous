def factorial(n):
    r = 1
    for f in range(1, n+1):
        r = r * f
    return r
def divisors(n):
    ds = []
    for d in range(n):
        print(n % (d+1), d)
        if n % (d+1) == 0:
            print("Divisible by", d+1)
            ds.append(d+1)
        else:
            print("Not divisible by", d + 1)
    return ds
while True:
    n = int(input("Enter number to factorial: "))
    print(factorial(n))
    print("The divisors of the factorial are", divisors(n))
    print()
