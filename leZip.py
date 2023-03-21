import tkinter as tk


#track = [["|"]*20][:]*20
s = "|"
w = 32
h = 32
track = []
for y in range(h):
    a = []
    for x in range(w):
        a.append(s)
    track.append(a)
print(track)
#Phase 0 = start
#Phase 1 = "ready", same as Phase 0
#Phase 2 = "set", user sets track
#Phase 3 = "go", finalize track and start race.
phase = 0


def o1(track):
    r = []
    for o in track:
        r.extend(o)
    return r

def pt(X1, Y1, X2, Y2):
    '''Returns a list of x-y tuples of the positions passed through moving from X1, Y1 to X2, Y2'''
    if (X1,Y1) == (X2,Y2):
        return []
    if abs(X1-X2) < abs(Y1-Y2):
        x1 = Y1
        y1 = X1
        x2 = Y2
        y2 = X2
        swapped = True
    else:
        x1 = X1
        y1 = Y1
        x2 = X2
        y2 = Y2
        swapped = False
    m = (y2 - y1)/(x2-x1)
    #delta-y over delta-x, m=slope
    b = y1 - m*x1
    def f(x):
        return m*x + b
    r = [(x1,y1)]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if abs(y - f(x)) < 1:
                r.append((x,y))
    r.append((x2,y2))
    fr =[]
    for e in r:
        if swapped:
            e = (e[1],e[0])
        if e not in fr:
            fr.append(e)
    return fr
    

def iv(move, track):
    #r = True
    passed = pt(move[0][0], move[0][1], move[1][0], move[1][1])[1:]
    for p in passed:
        if track[p[1]][p[0]] == "|":
            return False
    return True

def pm(track, whosmove, vA, vB, steer):
    '''vA=xy tup of vel of A. vB=xy tup of vel of B. steer=xy tup of steering'''
    print("Have Reached PM")
    track = track[:]
    if whosmove == "A":
        v = vA
    else:
        v = vB
    v = (v[0]+steer[0], v[1]+steer[1])
    for rn in range(len(track)):
        for cn in range(len(track[rn])):
            if track[rn][cn] == whosmove:
                p = (cn, rn)
    t = (p[0]+v[0], p[1]+v[1])
    if t[1] > len(track):
        t = (t[0], len(track))
    if t[0] > len(track[0]):
        t = (len(track[0]), t[1])
    if iv((p,t),track):
        track[p[1]][p[0]] = "."
        track[t[1]][t[0]] = whosmove
        if whosmove == "A":
            return (track, v, vB)
        else:
            return (track, vA, v)
    ptbm = pt(p[0], p[1], t[0], t[1])
    ptbm.sort(key=lambda tt: ((((tt[0]) - (p[0])) ** 2) + (((tt[1]) - (p[1])) ** 2)) ** (1/2))
    t = p
    v = (0, 0)
    for n in range(1,len(ptbm)):
        if track[ptbm[n][1]][ptbm[n][0]] == "|":
            t = ptbm[n-1]
            break
    track[p[1]][p[0]] = "."
    track[t[1]][t[0]] = whosmove
    if whosmove == "A":
        return (track, v, vB)
    else:
        return (track, vA, v)
##    
##        for tt in pt(p[0], p[1], t[0], t[1]):
##            td = ((((tt[0]) - (p[0])) ** 2) + (((tt[1]) - (p[1])) ** 2)) ** (1/2)
##            if td < 
def dt(track):
    global buttons
    for y in range(len(track)):
        for x in range(len(track[y])):
            tfg = {".":"green", "|":"black", "A":"red", "B":"blue"}[track[y][x]]
            #print(track[y][x], end=" ")
            buttons[y * len(track[y]) + x]["background"] = tfg
        #print()
            
            

def wc(x,y):
    global track, phase
    if phase == 0:
        pass
    elif phase == 1:
        if o1(track).count("A") == 0: track[y][x] = "A"
        elif o1(track).count("B") == 0: track[y][x] = "B"
        else: pass
        #pass
    elif phase == 2:
        dt(track)
        print(y, x)
        print(track[y][x])
        track[y][x] = {"|":".", ".":"|", "A":"A", "B":"B"}[track[y][x]]
        print(track[y][x])
        dt(track)

ts = 0

def mm(track, whosmove, vA, vB, steer, ts):
    track, vA, vB = pm(track, whosmove, vA, vB, steer)
    
    if eval("v" + whosmove) == (0,0):
        ts = 3
        wm = {"A":"B", "B":"A"}[whosmove]
    if ts == 0:
        wm = {"A":"B", "B":"A"}[whosmove]
    else:
        ts = ts - 1
        try:
            eval(wm)
        except:
            wm = whosmove
    return (track, wm, vA, vB, ts)

def sb(c, dx, dy):
    global track, phase, wm, vA, vB, ts
    print("HERE")
    if phase == 3 and c == wm:
        print("Here too!", vA, vB, c, dx, dy)
        track, wm, vA, vB, ts = mm(track, c, vA, vB, (dx, dy), ts)
        print("Here three!", vA, vB)
        dt(track)
        

def np():
    global phase
    if phase < 3:
        phase = phase + 1

#wc(2, 2)
wm = "A"
vA = (1, 0)
vB = (1, 0)
ts = 0
root = tk.Tk()
bw = 2
(tk.Button(root, text="NEXT PHASE", command=np)).grid(column=(w//2)-2,row=h,columnspan=5)
buttons = []
for n in range(h*w):
    buttons.append("")
for x in range(w):
    for y in  range(h):
        b = tk.Button(root, text="", width=bw, height=bw//2, command=lambda x=x,y=y: wc(x, y))
        b.grid(row=y, column=x)
        buttons[y * w + x] = b

for c in "AB":
    for dx in range(-1,2):
        for dy in range(-1,2):
            (tk.Button(root, text="", width=bw, height=bw//2, background={"A":"red", "B":"blue"}[c], command = lambda c=c,dx=dx,dy=dy:sb(c,dx,dy))).grid(row={"A":1, "B":5}[c] + dy, column = w+5+dx)
tk.mainloop()


