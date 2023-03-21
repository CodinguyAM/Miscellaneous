def sqrt(x):
    return x**0.5

print("This is Advay's Heron's Formula Program!")
while True:
    print()
    strsides = input("Side lengths?").split(", ")
    sides = []
    for side in strsides:
        sides.append(eval(side))
    a = sides[0]
    b = sides[1]
    c = sides[2]

    s = (a + b + c)/2
    AREA = sqrt(s * (s - a) * (s - b) * (s - c))
    print(AREA)
