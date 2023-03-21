import tkinter as tk
from random import randint as ri
from random import choices as ch
BORDWEIGHT = 50
BATTWEIGHT = 100
CAPNWEIGHT = 2
INTRWEIGHT = 1


HEIGHT = 30
WIDTH  = 30
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
rth = rgbToHex
def neighbs(x, y, maxx=WIDTH, maxy=HEIGHT):
    return [(X[0] % maxx, X[1] % maxy) for X in [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1), (x, y)]]
def neighbcon(board, x, y):
    return [board[I[1]][I[0]][0] for I in neighbs(x, y)]
def squaretype(board, x, y, coi, atwars, capitals):
    if board[x][y] in (0, 1):
        return 0
    coien = atwars[coi]
    cap = capitals[coi]
    global BORDWEIGHT, BATTWEIGHT, INTRWEIGHT, CAPNWEIGHT
    if board[y][x][0] != coi:
        return 0
    elif len(list(set(neighbcon(board, x, y)))) > 1 and len(set(neighbcon(board, x, y)).intersection(coien)) == 0:
        return BORDWEIGHT
    elif len(list(set(neighbcon(board, x, y)))) > 1 and len(set(neighbcon(board, x, y)).intersection(coien)) >= 1:
        return BATTWEIGHT
    elif (x, y) in neighbs(cap[0], cap[1]):
        return CAPNWEIGHT
    else:
        return INTRWEIGHT
def disp(board, buttons):
    b = board[:]
    global COLOURS, CAPITALS, atwars, ntkG
    ntkG.destroy()
    atw = atwars
    clr = COLOURS
    for y in range(len(b)):
        #print(b[y], "BY")
        for x in range(len(b[y])):
            buttons[y][x]['text'] = b[y][x][1]
            if type(b[y][x][0]) == type([]):
                b[y][x] = (b[y][x][0][0], b[y][x][1])
            if (x, y) in CAPITALS.values():
                buttons[y][x]['font'] = 'serif 8 bold'
            buttons[y][x]['bg']=clr[b[y][x][0]]
    ntk = tk.Toplevel()
    rn = 0
    for c in atwars.keys():
        cn = 1
        (tk.Button(ntk, bg=clr[c])).grid(row=rn, column=0)
        for c2 in atw[c]:
            (tk.Button(ntk, bg=clr[c2])).grid(row=rn, column=cn)
            cn = cn + 1
        rn = rn + 1
    ntkG = ntk
def sme(board):
    global atwars, CAPITALS
    for y in range(len(board)):
        for x in range(len(board[y])):
            coi = board[y][x][0]
            if coi not in (0, 1):
                for s in range(board[y][x][1]):
                    wd = []
                    for T in neighbs(x, y):
                        stw=squaretype(board, T[0], T[1], coi, atwars, CAPITALS)
                        if stw > 0:
                            stw = stw + (50 - board[T[1]][T[0]][1])/50
                        wd.append(stw)
                    if sum(wd) > 0:
                        #print('MOVING', coi)
                        while True:
                            np = ch(neighbs(x, y), weights=wd)[0]
                            #print(np)
                            #print(len(board), np[1], ',', len(board[0]), np[0], ',', )
                            if board[np[1]][np[0]][0] not in (0,1):
                                break
                        board[np[1]][np[0]] = (board[np[1]][np[0]][0], board[np[1]][np[0]][1] + 1)
                        board[y][x] = (coi, board[y][x][1] - 1)
                            
    return board
def oce(board):
    b = board
    neb = []
    for row in board:
        neb.append(row[:])
    global atwars, CAPITALS
    destcount =[]
    for y in range(len(b)):
        
        
        for x in range(len(b[y])):
            prevO = b[y][x][0]
            w = {}
            for n in neighbs(x, y):
                #print(b[n[1]][n[0]][0])
                if type(b[n[1]][n[0]][0]) == type([]):
                    b[n[1]][n[0]] = (b[n[1]][n[0]][0][0], b[n[1]][n[0]][1])
                if b[n[1]][n[0]][0] in atwars[prevO]:
                    
                    if b[n[1]][n[0]][0] in w.keys():
                        w[b[n[1]][n[0]][0]] = w[b[n[1]][n[0]][0]] + b[n[1]][n[0]][1]
                    else:
                        w[b[n[1]][n[0]][0]] = b[n[1]][n[0]][1]
            cWC = []
            W = []
            for X in w.keys():
                cWC.append(X)
                W.append(w[X])
            if prevO not in (0, 1):
                cWC.append(prevO)
                W.append(200)
            if sum(W) > 0:
                newO = ch(cWC, weights=W)[0]
                s = b[y][x][1]
                if prevO == 0:
                    s = 10
                #print(newO, prevO, (x, y), (x, y) in CAPITALS.values(), newO != prevO)
                if newO != prevO and (x, y) in CAPITALS.values():
                    destcount.append(prevO)
                neb[y][x] = (newO, s)
    for y in range(len(neb)):
        for x in range(len(neb[y])):
            if neb[y][x][0] in destcount:
                neb[y][x] = (0, 0)
    return neb

def wpe(atwars):
    n = atwars
    for c in atwars.keys():
        if c not in (0, 1):
            for c2 in atwars[c]:
                if ri(0, 100) < 10 and c2 not in (0, 1, c):
                    n[c].remove(c2)
                    n[c2].remove(c)
            for c3 in atwars.keys():
                if ri(0, 100) < 10 and c3 not in (0, 1, c):
                    n[c].append(c3)
                    n[c3].append(c)
    for k in n.keys():
        n[k] = list(set(n[k]))
    return n
HEIGHT = 30
WIDTH  = 30
BOARD = []
for y in range(HEIGHT):
    ta = []
    for x in range(WIDTH):
        ta.append((0, 0))
    print(ta)
    BOARD.append(ta)
atwars = {0:[], 1:[]}
index = 2
CLICKMODE = 'k'
COLOURS = {0:rth((127,127,127)), 1:rth((0, 0, 255))}
CAPITALS = {}
BUTTONS = []
root = tk.Tk()
ntkG = tk.Toplevel()
def wc(bx, by):
    global BOARD, CLICKMODE, index, WIDTH, HEIGHT, BUTTONS, COLOURS, CAPITALS, atwars
    if CLICKMODE == 'LAND':
        BOARD[by][bx] = (0, 0)
    elif CLICKMODE == 'WATER':
        BOARD[by][bx] = (1, 0)
    elif CLICKMODE == 'k':
        for n in neighbs(bx,by):
            BOARD[n[1]][n[0]] = (index + 1, 4)
        atwars[0] = atwars[0]  + [index+1]
        atwars[index+1] = [0]
        CAPITALS[index+1] = (bx, by)
        COLOURS[index+1] = rgbToHex((ri(1, 255), ri(1, 255), ri(1, 255)))
        index = index+1
    disp(BOARD, BUTTONS)
for y in range(HEIGHT):
    a = []
    for x in range(WIDTH):
        aa = tk.Button(root, width=2, height=1, command=lambda   x=x, y=y: wc(x, y))
        aa.grid(row=y, column=x)
        a.append(aa)
    BUTTONS.append(a)
tl = tk.Toplevel()
def evevha():
    global BUTTONS, BOARD, atwars
    BOARD = sme(BOARD)
    print('SM')
    disp(BOARD, BUTTONS)
    BOARD = oce(BOARD)
    print('OC')
    disp(BOARD, BUTTONS)
    atwars = wpe(atwars)
    print('WP')
def lev():
    global CLICKMODE
    CLICKMODE = 'WATER'
def wev():
    global CLICKMODE
    CLICKMODE = 'LAND'
def kev():
    global CLICKMODE
    CLICKMODE = 'k'

b = tk.Button(tl, text='sme', command=evevha)
b.grid(row=0, column=0)
(tk.Button(tl, text='evolve', command=lev)).grid(row=0,column=1)
(tk.Button(tl, text='water', command=wev)).grid(row=0,column=2)
(tk.Button(tl, text='kingdom', command=kev)).grid(row=0,column=3)
