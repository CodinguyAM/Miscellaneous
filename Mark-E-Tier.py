import random

def evMarket(cp, ce):
    re = []
    rp = []
    for p in range(len(cp)):
        r = random.random()
        if r < 1/3:
            rp.append((1 + (-1 * r * 3/4)) * cp[p])
        if r > 2/3:
            return (1 + (1 - r) * 3/4)
        else:
        
