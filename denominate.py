

cachy = {}
cache2 = {}

def fills(n, den=[1, 5, 10, 25], collapses=None):
    global cache2
    if (n, tuple(den)) in cachy.keys():
        return cache2[(n, tuple(den))]
    if collapses==None:
        collapses = c(den)
    print(collapses)
    #print(n)
    if min(den) > 1:
        return []
    r = []
    if n == 0:
        return [[]]
    if n in den:
        return [[n]]
    for d in den:
        if d <= n:
            ps = fills(n - d, den)
            for s in ps:
                if (s.count(d) + 1) * d in den and s.count(d) > 0:
                    continue
                if isIn([d] + s, r):
                    continue
                a = [d] + s
                r.append(a)
    cache2[tuple([n, tuple(den)])] = r
    return r


def eff_fills(n, den=[1, 5, 10, 25], collapses=None):
    global cachy
    if (n, tuple(den)) in cachy.keys():
        return cachy[(n, tuple(den))]
    if collapses==None:
        collapses = c(den)
    #print(collapses)
    #print(n)
    if min(den) > 1:
        raise ValueError
    r = []
    if n == 0:
        return [[]]
    if n in den:
        return [[n]]
    for d in den:
        if d <= n:
            ps = eff_fills(n - d, den, collapses)
            for s in ps:
                if (s.count(d) + 1) * d in den and s.count(d) > 0:
                    continue
                if isIn([d] + s, r):
                    continue
                a = [d] + s
                r.append(a)
    cachy[(n, tuple(den))] = [min(r,key=len)]
    return [min(r,key=len)]

def areEqual(l1, l2):
    return sorted(l1) == sorted(l2)

def isIn(dbt, tchk):
    r = False
    for n in tchk:
        if areEqual(n, dbt):
            r = True
    return r

def shortest(n, den=[1,5,10,25]):
    s= fills(n, den)
    return len(min(s, key=len))

def c(den):
    r = {}
    for d in den:
        for d2 in den:
            if d % d2 == 0:
                r[d2] = r.get(d2, [])+ [d/d2]
    return r

while True:
    try:
        n = int(input('Level: '))
        dn = input('Denominations? (seperate by commas): ').split(',')
        den = []
        for d in dn:
            den.append(int(d))
        moves = {}
        for x in range(1, n+1):
            moves[x] = len(eff_fills(x, den)[0])
            print(moves[x], 'moves for', x , 'cents')
        print('Denomination Efficiency Score (DES):', round(((round((1/(len(den)*sum(list(moves.values())))) * 1000 * n)) - (len(den) * (200/(n+1)))) * 2))
        print('Total Coinage:',  sum(list(moves.values())))
        print()
    except:
        print('PLEASE ENTER PROPERLY FORMATTED INPUT QA')
        print()
        continue
#        
            
        
