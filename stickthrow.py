import random as r

def OOF(p0):
    rn = r.random()
    if rn < p0:
        return "0"
    else:
        return "1"

def bw(s):
    t = ""
    for i in s:
        if i == "0":
            t = t + "Black, "
        else:
            t = t + "White, "
    return t

def f():
    return bw(OOF(0.5))

while True:
    input("Flip?: ")
    print(f(), f(), f(), f())
    print()
