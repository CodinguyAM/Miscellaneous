import random
import tkinter as tk

h = 19
w = 19
heights = [0] * h * w

def ne(n, h, w, m="SHVeD"):
    m = m.lower()
    r = []
    if "s" in m:
        r.append(n)
    if (n % w) > 0:
        if "h" in m: r.append(n - 1)
        if "d" in m:
            if (n > w):
                r.append(n - 1 - w)
        if "e" in m:
            if (n < ((h - 1) * w)):
                r.append(n - 1 + w)
    if (n % w) < w - 1:
        if "h" in m:
            r.append(n + 1)
        if "d" in m:
            if (n < ((h - 1) * w)):
                r.append(n + 1 + w)
        if "e" in m:
            if (n < ((h - 1) * w)):
                r.append(n - 1 + w)
    if n >= w:
        r.append(n - w)
    if n < ((h - 1) * w):
        r.append(n + w)
    return r

def ene(l, h, w, m="SHVeD"):
    r = []
    for x in l:
        r.extend(ne(x, h, w, m))
    return r

def flatdisp(alloc, h, w):
    for x in range(h * w):
        print( alloc[x], end=(' '*(3-(len(str( alloc[x] ))))) )
        if x % w == w - 1:
            print()

def eneE(l, h, w, a, m="SHVeD"):
    r = []
    for x in l:
        if set([a[y] for y in ne(x)]) == set([-1]):
            break
        r.extend(ne(x))

def sphm(p, h, w):
    cores = []
    plates = []
    for x in range(p):
        cores.append(int(random.random() * h * w))
        plates.append([cores[x]])
    alloc = [-1] * h * w
    while alloc.count(-1):
        flatdisp(alloc, h, w)
        print()
        for pli in range(len(plates)):
            pl = plates[pli]
            pln = eneE(pl, h, w, alloc)
            plncpy = eneE(pl, h, w, alloc)
            for sq in plncpy:
                if alloc[sq] != -1:
                    pln.remove(sq)
            for sq in pln:
                alloc[sq] = pli
            plates[pli] = pln
    return (alloc, plates)

def disp(alloc, clrs):
    root = tk.Toplevel()
    for x in range(len(alloc)):
        tq = tk.Button(bg=clrs[alloc[x]])
        tq.grid(row=x//w, column=x%w)
    return root

p = 5

base = sphm(p, h, w)
print('base generated')
disp(base[0], ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta'])
