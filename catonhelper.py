import random

def p(p0):
    r = random.random()
    return (r < p0)

while True:   
    m = int(input('Mountain tiles: '))
    f = int(input('Forest tiles: '))
    ores = 0
    for x in range(m):
        ores = ores + int(p(0.5))
    print(ores, "metals")
    ores = 0
    for x in range(f):
        ores = ores + int(p(0.9))
    print(ores, "woods")
    print()
