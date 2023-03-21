from random import choices as ch
from random import randint as ri
import tkinter as tk
def rgbToHex(c):
    r,g,b = c
    r = int(r)
    g = int(g)
    b = int(b)
    #remove the 0x
    hexR = hex(r)[2:]
    if len(hexR) == 1:
        hexR = '0' + hexR
    elif len(hexR) == 0:
        hexR = '00'
    hexG = hex(g)[2:]
    if len(hexG) == 1:
        hexG = '0' + hexG
    elif len(hexR) == 0:
        hexG = '00'
    hexB = hex(b)[2:]
    if len(hexB) == 1:
        hexB = '0' + hexB
    elif len(hexR) == 0:
        hexB = '00'
    return "#" + hexR + hexG + hexB

def neighbsquares(x,y, mx,my,mode='hv'):
    r = [(x,y)]
    for c in mode:
        if c == "h":
            r.extend([(x+1,y), (x-1,y)])
        elif c == "v":
            r.extend([(x,y+1), (x,y-1)])
        elif c == "d":
            r.extend([(x+1,y+1), (x-1, y-1), (x+1,y-1), (x-1, y+1)])
    rr = []
    for e in r:
        rr.append((e[0] % mx, e[1] % my))
    return rr

def squaretype(board,x,y,mx,my,coi,coi_enemies, mode="hv"):
    #Key:
    #A - Not part of Country of Interest(CoI)
    #B - Border in CoI
    #C - Battlefield in CoI
    #D - Interior of CoI
    mx = len(board[0])
    my = len(board)
    if coi == 'unclaimed':
        return 'A'
    if board[y][x][0] != coi:
        return "A"
    if len(list(set([tuple(str(board[S[1]][S[0]][0])) for S in neighbsquares(x, y, mx, my, mode)]))) > 1:
        isnotbf = True
        for n in [board[S[1]][S[0]] for S in neighbsquares(x, y, mx, my, mode)]:
            if n in coi_enemies:
                isnotbf = False
        if isnotbf:
            return "B"
        else:
            return "C"
    else:
        return "D"

def sme(board, atwars, mode="hv"):
    b = board[:]
    r = board[:]
    mx = len(b[0])
    my = len(b)
    print(mx, my)
    for y in range(len(b)):
        for x in range(len(b[y])):
            coi = b[y][x][0]
            if type(coi) == type([]): coi = coi[0]
            if coi == 'unclaimed':
                continue
            for s in range(b[y][x][1]):
                w = []
                for n in neighbsquares(x, y, mx, my, mode):
                    stype = squaretype(b,x,y,mx,my,coi,atwars[coi],mode)
                    w.append(max((({"A":0, "B":2, "C":3, "D":1}[stype] * 10) - b[n[1]][n[0]][1]), 0.00000000000000000001))
                ns = ch(neighbsquares(x, y, mx, my, mode), weights=w)[0]
                #print(ns)
                r[ns[1]][ns[0]] = (r[ns[1]][ns[0]][0], r[ns[1]][ns[0]][1] + 1)
                r[y][x] = (r[y][x][0], r[y][x][1] - 1)
                
    return r

def oce(board, atwars, capitals, mode="hv"):
    b = board[:]
    r = board[:]
    mx = len(b[0])
    my = len(b)
    destcount = []
    for y in range(len(b)):
        for x in range(len(b[y])):
            po = b[x][y][0]
            if type(po) == type([]):
                po = po[0]
            if po != 'uncaimed':
                #print("NS:", po, 'at', x,y)
                weights_d = {}
                for n in neighbsquares(x, y, mx, my, mode):
                    #print(n, b[n[1]][n[0]][0], po)
                    #print(neighbsquares(x, y, mx, my, mode))
                    if b[n[1]][n[0]][0] not in ['unclaimed', ['unclaimed']]:
                            
                        if b[n[1]][n[0]][0] in atwars[po] or b[n[1]][n[0]][0] == po:
                            weights_d[b[n[1]][n[0]][0]] = weights_d.get(b[n[1]][n[0]][0], 0) + b[n[1]][n[0]][1]
                            #print(po)
                cwc = list(weights_d.keys())
                w = []
                for c in cwc:
                    w.append(weights_d[c])
                if set(w) == set([0]):
                    no = po
                else:
                    if w != []:
                        no = ch(cwc, weights=w)
                    else:
                        no = 'unclaimed'
                if po == 'unclaimed' and no != 'unclaimed':
                    r[y][x] = (r[y][x][0], 3)
                elif po == 'lake':
                    pass
                elif no != po and (x, y) == capitals[po]:
                    destcount.append(po)
                if no == 'unclaimed':
                    no = po
                r[y][x] = (no, r[y][x][1])
    for y in range(len(r)):
        for x in range(len(r[y])):
            if type(r[y][x][0]) == type([]):
                r[y][x] = (r[y][x][0][0], r[y][x][1])
            if r[y][x][0] in destcount:
                r[y][x] = ('unclaimed', 0)
    return r
            

def evolve(board, atwars, capitals, mode="hv"):
    board2 = sme(board, atwars, mode)
    board3 = oce(board2, atwars, capitals, mode)
    return board3

def disp(board, clr, buttons):
    b = board[:]
    for y in range(len(b)):
        for x in range(len(b[y])):
            buttons[y][x]['text'] = b[y][x][1]
            if type(b[y][x][0]) == type([]):
                b[y][x] = (b[y][x][0][0], b[y][x][1])
            buttons[y][x]['bg']=clr[b[y][x][0]]


h = 30
w = 30
t = []
for y in range(h):
    ta = []
    for x in range(w):
        ta.append(('unclaimed', 0))
    print(ta)
    t.append(ta)
print(t[1][0][0])
atwars = {'unclaimed': [], 'lake': []}
index = 0
cm = 'k'
clr = {'unclaimed':'grey', 'lake':'blue'}
capitals = {}
mode = 'hvd'
buttons = []
root = tk.Tk()
def wc(bx, by):
    global t, cm, index, mode, w, h, buttons, clr
    if cm == 'u':
        t[by][bx] = ('unclaimed', 0)
    elif cm == 'l':
        t[by][bx] = ('lake', 0)
    elif cm == 'k':
        for n in neighbsquares(bx,by,w,h,mode):
            t[n[1]][n[0]] = (index + 1, 4)
        atwars['unclaimed'] = atwars['unclaimed']  + [index+1]
        atwars[index+1] = ['unclaimed']
        capitals[index+1] = (bx, by)
        clr[index+1] = rgbToHex((ri(1, 255), ri(1, 255), ri(1, 255)))
        index = index+1
    disp(t, clr, buttons)

for y in range(h):
    a = []
    for x in range(w):
        aa = tk.Button(root, width=2, height=1, command=lambda   x=x, y=y: wc(x, y))
        aa.grid(row=y, column=x)
        a.append(aa)
    buttons.append(a)

def evevha():
    global t, mode, buttons, atwars, capitals
    t = evolve(t, atwars, capitals, mode)
    disp(t, clr, buttons)

def rev(n):
    for i in range(n):
        evevha()

(tk.Button(root, text="EVOLVE", command=evevha)).grid(row=h, column=w+3)
(tk.Button(root, text="EVOLVEx5", command=lambda:rev(5))).grid(row=h, column=w+4)
(tk.Button(root, text="EVOLVEx50", command=lambda:rev(50))).grid(row=h, column=w+5)
(tk.Button(root, text="EVOLVEx500", command=lambda:rev(500))).grid(row=h, column=w+6)


    
