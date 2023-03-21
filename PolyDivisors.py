def lplt(base, number):
    p = 0
    while True:
        if base ** p > number:
            return p - 1
        p = p + 1

def convert(base, number):
    r = []
    if number < base:
        return [number]
    bundles = int(number/base)
    r.append(number - base*bundles)
    r.extend(convert(base, bundles))
    return r
    
def convdisp(i, hush=False, addline=True):
    j = i[::-1]
    for k in j:
        if len(str(k)) > 1:
            if k > 9 and k < 36 and hush:
                print("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[k - 10], end="")
            else:
                print("[" + str(k) + "]", end="")
        else:
            print(k, end="")
    if addline:
        print()

def toBase10(base, number):
    r = 0
    for i in range(len(number)):
        r = r + number[i]*(base**i)
    return r

def nexts(base, cur, rem):
    r = []
    for i in rem:
        if toBase10(base, [i] + cur) % len([i] + cur) == 0:
            r.append(i)
    return r


def findPDs(base):
    rem = list(range(1, base))
    cur = []
    solutions = set([])
    everyView = {tuple(cur):list(range(1, base))}
    while everyView[tuple([])] != []:
        if len(cur) == base-1:
            solutions = solutions | set([tuple(cur)])
            break
        if tuple(cur) in everyView.keys():
            if everyView[tuple(cur)] == []:
                everyView[tuple(cur[1:])] = everyView[tuple(cur[1:])][1:]
                rem.append(cur[0])
                cur = cur[1:]
                continue
            else:
                del rem[rem.index(everyView[tuple(cur)][0])] 
                cur = [everyView[tuple(cur)][0]] + cur
        else:
            everyView[tuple(cur)] = nexts(base, cur, rem)
    return solutions

findingBase = 2
while True:
    print("Found a solution in base", findingBase)
    solutionsInBase = findPDs(findingBase)
    for s in solutionsInBase:
        convdisp(s, hush=True, addline=False)
        print(" or", toBase10(findingBase, s), "in decimal")
    print()
    findingBase = findingBase + 1
    
            
    

#convdisp(convert(12, 1726), hush=True)
#print(toBase10(2, [1, 0, 1, 1, 0]))
