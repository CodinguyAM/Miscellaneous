import tkinter as tk

def properFormat(maze):
    r = []
    r.append(["|"] * (len(maze[0])+2))
    for row in maze:
        r.append(["|"] + row + ["|"])
    r.append(["|"] * (len(maze[0])+ 2))
    return r
def o1l(m):
    r = []
    for o in m:
        for e in o:
            r.append(e)
    return r

def dt(track):
    global buttons
    for y in range(len(track)):
        for x in range(len(track[y])):
            tfg = {"L":"green", "W":"blue"}[track[y][x]]
            #print(track[y][x], end=" ")
            buttons[y * len(track[y]) + x]["background"] = tfg
        #print()


def erode(c):
    n = c[:]
    c = properFormat(c)
    for r in range(len(n)):
        for l in range(len(n[r])):
            if "W" in (c[r+1-1][l+1], c[r+1+1][l+1], c[r+1][l+1-1], c[r+1][l+1+1]):
                n[r][l] = "W"
    return n


def wc(x, y):
    global track
    dt(track)
    print(y, x)
    print(track[y][x])
    track[y][x] = {"W":"L","L":"W"}[track[y][x]]
    print(track[y][x])
    dt(track)
    

##dispMaze(t)
##            
##dispMaze(erode(t))
h = 30
w = 30
bw = 2
root = tk.Tk()
s = "L"
track = []
buttons =[]
for n in range(h*w):
    buttons.append("")
for y in range(h):
    a = []
    for x in range(w):
        a.append(s)
    track.append(a)
for x in range(w):
    for y in  range(h):
        b = tk.Button(root, text="", width=bw, height=bw//2, command=lambda x=x,y=y: wc(x, y))
        b.grid(row=y, column=x)
        buttons[y * w + x] = b
def f():
    global track
    track = erode(track)
    dt(track)
(tk.Button(root, text="ERODE", command=f)).grid(column=(w//2)-2,row=h,columnspan=5)
