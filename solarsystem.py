import seaborn
import pandas
import matplotlib.pyplot as plot
import tkinter as tk

def evolve(currobj, immov=[], G=1, e=0.1, halfe=False, rel=False):
    
    ret = currobj[:]
    c = currobj[:]
    for n in range(len(c)):
        if n not in immov:
            m = c[n][0]
            x = c[n][1][0]
            y = c[n][1][1]
            vx = c[n][2][0]
            vy = c[n][2][1]
            
            tax = 0
            tay = 0

            
            for o in range(len(c)):
                x0 = c[o][1][0]
                y0 = c[o][1][1]
                r = (((x - x0) ** 2) + ((y - y0) ** 2)) ** (1/2)
                M = c[o][0]
                if o != n:
                    print(ret[n][1], ret[n][2])
                    aM = G*M/(r**2)
                    ax = -1 * aM * (x-x0)/r
                    ay = -1 * aM * (y-y0)/r
                    tax = tax + ax
                    tay = tay + ay

            nvx = vx + e*tax
            nvy = vy + e*tay
            if halfe:
                avx = (vx + nvx)/2
                avy = (vy + nvy)/2
            else:
                avx = nvx
                avy = nvy
            nx = x + e*avx
            ny = y + e*avy
            ret[n][0] = m
            ret[n][1] = [nx, ny]
            ret[n][2] = [nvx, nvy]
    return ret

def further(track, immov, G=1, e=0.1):
    track.append(evolve(track[-1], immov, G, e))

def food(track):
    #Cloumn 0 = x, Column 1 = y, Column 2 = object
    r = []
    for s in track:
        t = 0
        for u in s:
            r.append([u[1][0], u[1][1], str(t)])
            t = t + 1
    return r


def disp(track):
    seaborn.scatterplot(data=pandas.DataFrame(food(track)), x=0,y=1,hue=2,legend=False,style=2)
    plot.show()

start = []
planets = int(input('How Many Planets?: '))
for n in range(planets):
    m = float(input('Mass of Obj ' + str(n+1) + ': '))
    x = float(input('X-Coord of Obj ' + str(n+1) + ': '))
    y = float(input('Y-Coord of Obj ' + str(n+1) + ': '))
    vx = float(input('X-Velocity of Obj ' + str(n+1) + ': '))
    vy = float(input('Y-Velocity of Obj ' + str(n+1) + ': '))
    start.append([m,[x,y],[vx,vy]])
    print()
print()
immvs = int(input('How many are immovable?: '))
immov = []
for o in range(immvs):
    r= int(input(str(o+1) + ' immovable object is obj no.: ')) - 1
    immov.append(r)
##start = [[10, [0, 0], [0, 0]], [1, [5, 0], [0, 1]]]
##immov = [0]
track = [start]
count = 0
def evevha():
    global track, immov, count
    further(track, immov)
    print(count)
    count = count + 1
    disp(track)
def rev(n):
    def f():
        for x in range(n):
            evevha()
    return f
root = tk.Tk()
(tk.Button(root, text='MOVE', command=evevha)).grid(row=0, column=0)

(tk.Button(root, text='MOVEx5', command=rev(5))).grid(row=1, column=0)

(tk.Button(root, text='MOVEx10', command=rev(10))).grid(row=0, column=1)

(tk.Button(root, text='MOVEx50', command=rev(50))).grid(row=1, column=1)

(tk.Button(root, text='MOVEx100', command=rev(100))).grid(row=2, column=1)

(tk.Button(root, text='MOVEx500', command=rev(500))).grid(row=2, column=0)

(tk.Button(root, text='MOVEx1000', command=rev(1000))).grid(row=2, column=2)

(tk.Button(root, text='MOVEx5000', command=rev(5000))).grid(row=1, column=2)

(tk.Button(root, text='MOVEx10000', command=rev(1000))).grid(row=0, column=2)







#disp(track)
    
    
#a = GM/r^2
#(GM/r^2)/(r) = -(ax)/(rx) = -(ay)/(ry)
#-(GMrx)/(r^3) = ax
#-(GMry)/(r^3) = ay
#vxNEW = vx - (eGMrx)/(r^3)
#vyNEW = vy - (eGMry)/(r^3)
#


                
        
    
