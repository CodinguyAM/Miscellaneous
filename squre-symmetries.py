#Inputs to I,V,H,D are to be in clockwise order from top left

def I(x):
    #identity
    #A B __\ A B
    #D C   / D C
    a,b,c,d = x
    return (a,b,c,d)

def V(x):
    #vertical flip
    #A B __\ D C
    #D C   / A B
    a,b,c,d = x
    return (d,c,b,a)

def H(x):
    #horizontal flip
    #A B __\ B A
    #D C   / C D
    a,b,c,d = x
    return (b,a,d,c)

def D(x):
    #diagonal flip from top-left
    #A B __\ A D
    #D C   / B C
    a,b,c,d = x
    return (a,d,c,b)

def E(x):
    #diagonal flip from top-right
    #A B __\ C B
    #D C   / D A
    a,b,c,d = x
    return (c,b,a,d)

def R(x):
    #rotate clockwise. for counterclockwise, use RRR
    #A B __\ D A
    #D C   / C B
    a,b,c,d = x
    return (d,a,b,c)

def disp(s):
    print()
    print(s[0] + " " + s[1])
    print()
    print(s[3] + " " + s[2])
    print()

x = ("A", "B", "C", "D")
disp(x)
while True:
    a = input("Which action do you choose? Your options are: I: Identity, V: Vertical flip, H: Horizontal flip, D and E: the two diagonals, R: rotate: ")
    x = eval(a + "(" + str(x) + ")")
    disp(x)
