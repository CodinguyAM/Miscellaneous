import random
import tkinter as tk

def score(board):
    score = 0
    for y in range(len(board)):
        for x in range(len(board)):
            if x < len(board[y]) - 1:
                if board[y][x] == board[y][x + 1]:
                    score = score + 2*board[y][x]
            if y < len(board) - 1:
                if board[y][x] == board[y + 1][x]:
                    score = score + 2*board[y][x]
    return score

def disp(boards, tomove, diceroll, nos):
    n = len(boards)
    b = boards[tomove % n]
    h = len(b)
    w = len(b[0])
    r = tk.Toplevel()
    r.geometry('300x300')
    l = []
    print(n,h,w, tomove)
    def f(v, u, d, q, k, c):
        i = k[v][u]
        if c[0]:
            k[q[0]][q[1]]['text'] = ''
        else:
            c[0] = True
        if i['text'] == '':
            i['text'] = d
            q[0] = v
            q[1] = u
        
        
       
    if tomove >= h * w * n:
        o = 0
        for z in sorted(list(range(n)), key=lambda e: score(boards[e]), reverse=True):
            (tk.Label(r, text='Player %i got %i points' % (z + 1, score(boards[z])))).grid(column = 0, row = o)
            o = o + 1
        r.title('Neighbours! Winners: ')
    else:
        p = [0,0]
        t = [False]
        r.title( 'Neighbours! Player %i to play: ' % ((tomove % n) + 1))
        for x in range(w):
            a = []
            for y in range(h):
                g = tk.Button(r, text=b[y][x], bg='grey', height=1, width = 2, command=lambda v=x, u=y: f(v, u, diceroll, p, l, t))
                g.grid(column=x,row=y)
                a.append(g)
            l.append(a)
        (tk.Label(r, text = 'The dice say: %i ' % diceroll)).grid(row=h, column=0, columnspan=w*5)
        def okevha():
            if t[0]:
                b[p[1]][p[0]] = diceroll
                m = tomove + 1
                s = diceroll
                if m % n == 0:
                    s = random.randint(1, nos)
                r.destroy()
                disp(boards, m, s, nos)
        (tk.Button(r, text='OK', command=okevha)).grid(row=h+1, column=0, columnspan=w*5)

n = 2
h = 5
w = 5
nos = 6
b = []
for i1 in range(n):
    bta = []
    for i2 in range(h):
        rta = []
        for i3 in range(w):
            cta = ''
            rta.append(cta)
        bta.append(rta)
    b.append(bta)
disp(b, 0, random.randint(1, nos), nos)
                
            
    
    
