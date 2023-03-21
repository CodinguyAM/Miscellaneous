from tkinter import *

expre = ""

c = Tk()
c.title("Calculator")

eq = Text(c, height=4, width=12)
def add(num):
    global eq
    global expre
    expre = expre + str(num)
    eq.insert(END, str(num))
ans = Text(c, height=4, width = 12)
def do():
    global expre
    global ans
    ans.delete(1.0, END)
    ans.insert(END, str(eval(expre)))
def clr():
    global ans
    global eq
    global expre
    ans.delete(1.0, END)
    eq.delete(1.0, END)
    expre = ""
b1 = Button(c, text="1", command=lambda: add(1))
b2 = Button(c, text="2", command=lambda: add(2))
b3 = Button(c, text="3", command=lambda: add(3))
b4 = Button(c, text="4", command=lambda: add(4))
b5 = Button(c, text="5", command=lambda: add(5))
b6 = Button(c, text="6", command=lambda: add(6))
b7 = Button(c, text="7", command=lambda: add(7))
b8 = Button(c, text="8", command=lambda: add(8))
b9 = Button(c, text="9", command=lambda: add(9))
b0 = Button(c, text="0", command=lambda: add(0))
bDiv = Button(c, text="/", command=lambda: add("/"))
bMul = Button(c, text="*", command=lambda: add("*"))
bAdd = Button(c, text="+", command=lambda: add("+"))
bSub = Button(c, text="-", command=lambda: add("-"))
bExp = Button(c, text="exponent", command=lambda: add("**"))
bPar = Button(c, text="(", command=lambda: add("("))
bCPa = Button(c, text=")", command=lambda: add(")"))
bMod = Button(c, text="Remainder", command=lambda: add("%"))
bSol = Button(c, text="Solve", command=lambda: do())
bClr = Button(c, text="Clear", command=lambda: clr())

r = 2
col = 0

eq.grid(row=0, column=0, columnspan=4)
ans.grid(row=1, column=0, columnspan=4)
for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, bDiv, bMul, bAdd, bSub, bExp, bPar, bCPa, bMod, bSol, bClr]:
    b.grid(row=r, column=col)
    col = col + 1
    if col == 4:
        r = r + 1
        col = 0

c.mainloop()
