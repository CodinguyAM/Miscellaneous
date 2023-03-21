from copy import deepcopy as dc
import tkinter as tk

def findNeighbsOf(x, y, maxx, maxy, mode="dhv"):
    neighbs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
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

def fn(b, x, y, mx, my, mode="dhv"):
    n = findNeighbsOf(x, y, mx, my, mode)
    r = []
    for ne in n:
        r.append(b[ne[1]][ne[0]])
    return r

def evolve(board, mode="dhv"):
    r = dc(board)
    b = dc(board)
    mx = len(board[0])
    my = len(board)
    for x in range(mx):
        for y in range(my):
            s = b[y][x]
            n = fn(b, x, y, mx, my, mode)
            if s == 0:
                if n.count(1) == 3:
                    r[y][x] = 1
                else:
                    r[y][x] = 0
            elif s == 1:
                if n.count(1) == 2 or n.count(1) == 3:
                    r[y][x] = 1
                else:
                    r[y][x] = 0
    return r

def disp(board, buttons):
    for on in range(len(board)):
        o = board[on]
        for en in range(len(o)):
            e = {1:"black", 0:"white"}[o[en]]
            buttons[on][en]["bg"] = e

h = 30
w = 60
t = []
m = 'dhv'
for y in range(h):
    ta = []
    for x in range(w):
        ta.append(0)
    t.append(ta)
def evha(bx, by):
    global t, buttons
    t[by][bx] = {1:0,0:1}[t[by][bx]]
    disp(t, buttons)

buttons = []
root = tk.Tk()
for y in range(h):
    a = []
    for x in range(w):
        aa = tk.Button(root, width=2, height=1, command=lambda   x=x, y=y: evha(x, y))
        aa.grid(row=y, column=x)
        a.append(aa)
    buttons.append(a)

def evevha():
    global t, m, buttons
    t = evolve(t, m)
    disp(t, buttons)

def rev(n):
    global t
    for i in range(n):
        evevha()
def destroyy():
    global t,h,w,buttons
    t = []
    for y in range(h):
        ta = []
        for x in range(w):
            ta.append(0)
        t.append(ta)
    disp(t, buttons)
    
(tk.Button(root, text="EVOLVE", command=evevha)).grid(row=h, column=w+3)
(tk.Button(root, text="EVOLVEx5", command=lambda:rev(5))).grid(row=h, column=w+4)
(tk.Button(root, text="EVOLVEx50", command=lambda:rev(50))).grid(row=h, column=w+5)
(tk.Button(root, text="EVOLVEx500", command=lambda:rev(500))).grid(row=h, column=w+6)
(tk.Button(root, text="CLEAR", command=destroyy, bg='red')).grid(row=h+1, column=w+3)

