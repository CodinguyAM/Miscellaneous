

def nr(cur):
    l = len(cur)
    r = []
    for x in range(l-1):
        r.append(cur[x] + cur[x+1])
    r.append(cur[l-1])
    return r


def o1l(m):
    r = []
    for o in m:
        for e in o:
            r.append(e)
    return r

def pascal(n):
    n = n+ 1
    r = []
    cur = [0]*n + [1]
    for x in range(n):
        nc = nr(cur)
        r.append(cur)
        cur = nc
    return r


def d(b):
    maze= b
    maxLen = len(str(max(o1l(maze), key=lambda x: len(str(x))))) + 1
    #r = 0
    for row in maze:
        #c = 0
        for cell in row:
            if cell == 0:
                cell = " "
            print(cell, end=" "*(maxLen - len(str(cell))))
            #c = c + 1
        print()
        #r = r + 1

def f(x):
    return x % 10

def color(n, f):
    p = pascal(n)
    r =p[:]
    for y in range(len(p)):
        for x in range(len(p[y])):
            r[y][x] = f(p[y][x])
    return r

d(color(100, f))
