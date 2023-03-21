def do(poly, x):
    r = 0
    for i in range(len(poly)):
         r = r + poly[i]*(x**i)
    return r


def derive(poly):
    r = ()
    for i in range(1, len(poly)):
        r = r + (poly[i] * i, )
    return r

print(derive((0, 0, 1)))
print(do(
