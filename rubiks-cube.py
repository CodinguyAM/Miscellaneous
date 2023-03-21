def RA(s):
    r = []
    for x in range(len(s[0])):
        a = []
        for y in range(len(s)):
            a.append(s[y][x])
        r.append(a)
    return r


def ORA(s):
    ras = RA(s)
    r = []
    for o in ras[::-1]:
        r.append(o[::-1])
    return r

t = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
print(RA(t))

def TC(r):
    ret = [RA(r[0]),
         [r[2][0],
          r[1][1],
          r[1][2]],
         [r[3][0],
          r[2][1],
          r[2][2]],
         [r[4][0],
          r[3][1],
          r[3][2]],
         [r[0][0],
          r[4][1],
          r[4][2]],
         r[5]]
    return ret

def TCC(r):
    ret = [ORA(r[0]),
           [
         
