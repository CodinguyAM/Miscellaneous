def nod(x):
    return 2*x + 1
def halftau(d):
    n = 0
    r = 0
    while n < d:
        r = r + 4/nod(n)
        r = r - 4/nod(n+1)
        n = n + 2
    return r
print(halftau(int(input("Degree: "))))
