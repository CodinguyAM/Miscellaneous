from copy import deepcopy as dc
import tkinter as tk
def findNeighbsOf(x, y, maxx, maxy, mode="hv"):
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

def fn(b, x, y, mx, my, mode="hv"):
    n = findNeighbsOf(x, y, mx, my, mode)
    r = []
    for ne in n:
        r.append(b[ne[1]][ne[0]])
    return r

def evolve(board, mode="hv"):
    r = dc(board)
    b = dc(board)
    mx = len(board[0])
    my = len(board)
    for y in range(my):
        for x in range(mx):
            s = b[y][x]
            n = fn(b, x, y, mx, my, mode)
            if s == "G":
                if n.count("R") > 0:
                    if n.count("T") > 0:
                        r[y][x] = "T"
                    else:
                        r[y][x] = "R"
                else:
                    r[y][x] = "G"
            elif s == "R":
                if n.count("G") > 0:
                    if n.count("T") > 0:
                        r[y][x] = "T"
                    else:
                        r[y][x] = "R"
                else:
                    r[y][x] = "G"
            elif s == "T":
                if n.count("R"):
                    r[y][x] = "T"
                else:
                    r[y][x] = "G"

    return r

def disp(board, buttons):
    for on in range(len(board)):
        o = board[on]
        for en in range(len(o)):
            e = {"G":"green", "R":"white", "T":"orange"}[o[en]]
            buttons[on][en]["bg"] = e
h = 30
w = 30
t = []
m = 'hv'
for y in range(h):
    ta = []
    for x in range(w):
        ta.append('G')
    t.append(ta)
cursormode = "G"
def evha(bx, by):
    global cursormode, t, buttons
    t[by][bx] = cursormode
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

def gbeh():
    global cursormode
    cursormode = "G"
def rbeh():
    global cursormode
    cursormode = "R"
def tbeh():
    global cursormode
    cursormode = "T"
def evevha():
    global t, m, buttons
    t = evolve(t, m)
    disp(t, buttons)

def rev(n):
    global t
    for i in range(n):
        evevha()
(tk.Button(root, bg="green", text="GRASS", command=gbeh)).grid(row=h, column=w)
(tk.Button(root, bg="white", text="RABBITS", command=rbeh)).grid(row=h, column=w+1)
(tk.Button(root, bg="orange", text="TIGERS", command=tbeh)).grid(row=h, column=w+2)
(tk.Button(root, text="EVOLVE", command=evevha)).grid(row=h, column=w+3)
(tk.Button(root, text="EVOLVEx5", command=lambda:rev(5))).grid(row=h, column=w+4)
(tk.Button(root, text="EVOLVEx50", command=lambda:rev(50))).grid(row=h, column=w+5)
(tk.Button(root, text="EVOLVEx500", command=lambda:rev(500))).grid(row=h, column=w+6)
                
            
