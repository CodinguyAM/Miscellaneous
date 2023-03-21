import random
from copy import deepcopy as dc
import tkinter as tk
import time
from PIL import Image
import numpy as np
import pandas as pd

frame = 1
saveto = 'anbattle-fixd'


def rir(row):
    r = []
    for c in row:
        r.extend([{'red':(255,0,0),
                  'green':(0,255,0), 
                  'blue':(0,0,255), 
                  'yellow':(255,255,0),
                   '.':(127,127,127)}[c]]* 2)
    return [r, r]
def intorgb(board):
    r = []
    for row in board:
        r.extend(rir(row))
    return r
print(pd.DataFrame(intorgb([['green', '.', 'blue'],
                            ['.', '.', '.'],
                            ['red', '.', 'yellow']])))
def isBattlefield(board, x, y, mode="hv"):
    neighbs = findNeighbsOf(x, y, len(board[y]), len(board[x]), mode)
    ret = False
    nc = []
    for n in neighbs:
        countryat = board[n[1]][n[0]]
        cat = countryat
        if (not cat in nc) and (cat != '.') and (cat != '|'):
            nc.append(cat)
    return len(nc) > 1

def findNeighbsOf(x, y, maxx, maxy, mode="hv"):
    neighbs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x, y)]
    if mode in ("dhv", "hvd"):
        neighbs.extend([(x-1, y-1),
                        (x+1, y-1),
                        (x-1, y+1),
                        (x+1, y+1)])
    r = []
    for n in neighbs:
        if n[0] in range(0, maxx) and n[1] in range(0, maxy):
            r.append(n)
    return r

def fnc(b, x, y, mx, my, mode="hv"):
    n = findNeighbsOf(x, y, mx, my, mode)
    r = []
    for ne in n:
        if b[ne[1]][ne[0]] != ".":
            r.append(b[ne[1]][ne[0]])
    return r

def fn(b, x, y, mx, my, mode="hv"):
    n = findNeighbsOf(x, y, mx, my, mode)
    r = []
    for ne in n:
        r.append(b[ne[1]][ne[0]])
    return r

def evolve(board, mode="hv"):
    r = dc(board)
    b = dc(board)
    maxx = len(board[0])
    maxy = len(board)
    for x in range(maxx):
        for y in range(maxy):
            if isBattlefield(b, x, y, mode):
                nc = fnc(b, x, y, maxx, maxy, mode)
                r[y][x] = random.choice(nc)
            else:
                if set(fn(b, x, y, maxx, maxy, mode)) == set(['.']):
                    r[y][x] = b[y][x]
                else:
                    r[y][x] = list(set(fnc(b, x, y, maxx, maxy, mode)))[0]
    return r

def disp(board, buttons):
    for on in range(len(board)):
        o = board[on]
        for en in range(len(o)):
            e = o[en]
            if e == '.':
                e = 'grey'
            buttons[on][en]["bg"] = e
s = 30
n = []

for y in range(s-2):
    ta = []
    for x in range(s):
        ta.append('.')
    n.append(ta)
t = [['green'] + ['.']*(s-2) + ['blue']] + n + [['red'] + ['.']*(s-2) + ['yellow']]
m = "hvd"
h = len(t)
w = len(t[0])
playing = False
def evevha():
    global t, buttons, m, frame
    t = evolve(t, m)
    (Image.fromarray(np.asarray(intorgb(t)), mode='RGB')).save('C:\\Users\\advay\\Desktop\\Advay\\Python\\' + saveto + '\\frame%05d.jpg' % frame)
    frame = frame + 1
    
    disp(t, buttons)

def evevha5():
    for n in range(5):
        evevha()
        

def evevha50():
    for n in range(50):
        evevha()

def evevha500():
    for n in range(500):
        evevha()
buttons = []
root = tk.Tk()
for y in range(h):
    a = []
    for x in range(w):
        aa = tk.Label(root, width=2, height=1)
        aa.grid(row=y, column=x)
        a.append(aa)
    buttons.append(a)
disp(t, buttons)
(tk.Button(root, text="EVOLVE", command=evevha)).grid(row=h, column=w)
(tk.Button(root, text="EVOLVEx5", command=evevha5)).grid(row=h, column=w + 1)
(tk.Button(root, text="EVOLVEx50", command=evevha50)).grid(row=h, column=w + 2)
(tk.Button(root, text="EVOLVEx500", command=evevha500)).grid(row=h, column=w + 3)
tk.mainloop()








    

