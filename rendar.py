from math import sin, cos, tan, atan, acos, asin, pi, degrees, radians, atan2
from tkinter import Button, Tk, Label, PhotoImage

def sgn(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        raise ValueError

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

def mix(c1, c2, w1, w2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return (min((r1 * w1 + r2 * w2, 255)), min((g1 * w1 + g2 * w2, 255)), min((b1 * w1 + b2 * w2, 255)))
    

def magn(x,y):
    return (x**2 + y**2)**(1/2)

def polToRect(r, theta):
    return (r * cos(theta), r * sin(theta))

def rectToPol(x, y):
    r = magn(x, y)
    if y == 0:
        return (r, (pi/2 * sgn(x)) % (2 * pi))
    else:
        return (r, (atan2(y, x)) % (2 * pi))

def rot(x, y, theta):
    '''Rotates the point with Cartesian coords (x, y) theta degrees counter-clockwise'''
    thet_rad = radians(theta)
    inPol = rectToPol(x, y)
    inPol = (inPol[0], (inPol[1] - thet_rad) % (2 * pi))
    backToCart = polToRect(inPol[0], inPol[1])
    return backToCart

def rotXY(x, y, z, theta):
    '''Rotates the rectangular coordinates (x, y, z) theta degrees counter-clockwise in the XY plane'''
    xy = (x, y)
    new_xy = rot(x, y, theta)
    new_x, new_y = new_xy
    new_z = z
    return (new_x, new_y, new_z)

def rotYZ(x, y, z, theta):
    '''Rotates the rectangular coordinates (x, y, z) theta degrees counter-clockwise in the YZ plane'''
    yz = (y, z)
    new_yz = rot(y, z, theta)
    new_y, new_z = new_yz
    new_x = x
    return (new_x, new_y, new_z)

def rotXZ(x, y, z, theta):
    '''Rotates the rectangular coordinates (x, y, z) theta degrees counter-clockwise in the XZ plane'''
    xz = (x, z)
    new_xz = rot(x, z, theta)
    new_x, new_z = new_xz
    new_y = y
    return (new_x, new_y, new_z)

def transform(x, y, z, dx, dy, dz):
    return (x + dx, y + dy, z + dz)

def redner(px, py, pz, vx, vy, vz, xyangle, xzangle, yzangle):
    start = (px, py, pz)
    #n for new
    n1 = rotXY(start[0], start[1], start[2], xyangle* -1)
    n2 = rotXZ(n1[0], n1[1], n1[2], (90) - xzangle)
    n3 = rotYZ(n2[0], n2[1], n2[2], (90) - yzangle)
    n4 = transform(n3[0], n3[1], n3[2], -1 * vx, -1 * vy, -1 * vz)
    return n4

def render(points, vx, vy, vz, xyangle, xzangle, yzangle):
    r = []
    for point in points:
        px, py, pz = point
        rednered = redner(px, py, pz, vx, vy, vz, xyangle, xzangle, yzangle)
        rendered = ((rednered[0], rednered[1]), rednered[2])
        r.append(rendered)
    r.sort(key=lambda p: p[1])
    return r

def rendar(points, vx, vy, vz, xyangle, xzangle, yzangle, color_none, color_close, color_far, buttons):
    rendered = render(points, vx, vy, vz, xyangle, xzangle, yzangle)
    farthest_dist = max(rendered, key=lambda x: (x[1] * int(x[1] > 0)))[1]
    closest_dist = min(rendered, key=lambda x: x[1] * int(x[1] > 0))[1]
    diffdist = farthest_dist - closest_dist
    for b in buttons:
        b["background"] = rgbToHex(color_none)
    for rp in rendered:
        x = rp[0][0]
        y = rp[0][1]
        d = rp[1]
        if abs(x) < 50 and abs(y) < 50 and d > 0:
            nx = round(x * sgn(x)) * sgn(x) + 50
            ny = round(y * sgn(y)) * sgn(y) + 50
            n = ny * 100 + nx
            close = (d - closest_dist)/diffdist
            far = (farthest_dist - d)/diffdist
            prop_col = rgbToHex(mix(color_close, color_far, close, far))
            buttons[n]["bg"] = prop_col


def cube(x, y, z, s, step=1):
    
    r = []
    r.extend(XYsquare(x, y, z, s, step))
    r.extend(XZsquare(x, y, z, s, step))
    r.extend(YZsquare(x, y, z, s, step))
    r.extend(XYsquare(x, y, z + s, s, step))
    r.extend(XZsquare(x, y + s, z, s, step))
    r.extend(YZsquare(x + s, y, z, s, step))
    return r

def XYsquare(tx, ty, tz, s, step=1):
    r = []
    for x in range(tx, tx + s, step):
        for y in range(ty, ty + s, step):
            r.append((x, y, tz))
    return r

def XZsquare(tx, ty, tz, s, step=1):
    r = []
    for x in range(tx, tx + s, step):
        for z in range(tz, tz + s, step):
            r.append((x, ty, z))
    return r

def YZsquare(tx, ty, tz, s, step=1):
    r = []
    for z in range(tz, tz + s, step):
        for y in range(ty, ty + s, step):
            r.append((tx, y, z))
    return r





def topplingPyramid(tx, ty, tz, h, step=1):
    r = []
    for n in range(0, h, step):
        z = tz - n
        for x in range(tx, tx + n, step):
            for y in range(ty, ty + n, step):
                r.append((x, y, z))
    return r



def pyramid(tx, ty, tz, h, step=1):
    r = []
    for n in range(0, h, step):
        z = tz - n
        for x in range(tx - n, tx + n, step):
            for y in range(ty- n, ty + n, step):
                r.append((x, y, z))
    return r
        

vx = 0
vy = 0
vz = 0
xy = 0
xz = 90
yz = 90
p = cube(20, 20, 20, 30) + cube(21, 21, 21, 28)
#print(p)
cn = (255, 255, 255)
cc = (0, 255, 0)
cf = (255, 0, 0)


def VXp():
    global vx
    vx = vx + 1
    rndr()


def VXm():
    global vx
    vx = vx - 1
    rndr()


def VXsp():
    global vx
    vx = vx + 10
    rndr()


def VXsm():
    global vx
    vx = vx - 10
    rndr()


def VYp():
    global vy
    vy = vy + 1
    rndr()


def VYm():
    global vy
    vy = vy - 1
    rndr()


def VYsp():
    global vy
    vy = vy + 10
    rndr()


def VYsm():
    global vy
    vy = vy - 10
    rndr()


def VZp():
    global vz
    vz = vz + 1
    rndr()


def VZm():
    global vz
    vz = vz - 1
    rndr()


def VZsp():
    global vz
    vz = vz + 10
    rndr()


def VZsm():
    global vz
    vz = vz - 10
    rndr()


def XYp():
    global xy
    xy = xy
    rndr()


def XYm():
    global xy
    xy = xy - 1
    rndr()


def XYsp():
    global xy
    xy = xy + 10
    rndr()


def XYsm():
    global xy
    xy = xy - 10
    rndr()
    
def XZp():
    global xz
    xz = xz + 1
    rndr()


def XZm():
    global xz
    xz = xz - 1
    rndr()


def XZsp():
    global xz
    xz = xz + 10
    rndr()


def XZsm():
    global xz
    xz = xz - 10
    rndr()


def YZp():
    global yz
    yz = yz + 1
    rndr()


def YZm():
    global yz
    yz = yz - 1
    rndr()


def YZsp():
    global yz
    yz = yz + 10
    rndr()


def YZsm():
    global yz
    yz = yz - 10
    rndr()

def rndr():
    global vx, vy, vz, xy, xz, yz, p, cn, cc, cf, buttons
    rendar(p, vx, vy, vz, xy, xz, yz, cn, cc, cf, buttons)

if 1:

    root = Tk()
    buttons = []
    pixel = PhotoImage(width=1, height=1)
    for n in range(10000):
        b = Label(root, image=pixel, width=1, height=1)
        b.grid(row = n // 100, column = n % 100)
        buttons.append(b)



    (Button(root, text="X+", command=VXp)).grid(row=100 + 1, column= 100 + 1)
    (Button(root, text="X-", command=VXm)).grid(row=100 + 2, column= 100 + 1)
    (Button(root, text="X++", command=VXsp)).grid(row=100 + 3, column= 100 + 1)
    (Button(root, text="X--", command=VXsm)).grid(row=100 + 4, column= 100 + 1)
    (Button(root, text="Y+", command=VYp)).grid(row=100 + 1, column= 100 + 2)
    (Button(root, text="Y-", command=VYm)).grid(row=100 + 2, column= 100 + 2)
    (Button(root, text="Y++", command=VYsp)).grid(row=100 + 3, column= 100 + 2)
    (Button(root, text="Y--", command=VYsm)).grid(row=100 + 4, column= 100 + 2)
    (Button(root, text="Z+", command=VZp)).grid(row=100 + 1, column= 100 + 3)
    (Button(root, text="Z-", command=VZm)).grid(row=100 + 2, column= 100 + 3)
    (Button(root, text="Z++", command=VZsp)).grid(row=100 + 3, column= 100 + 3)
    (Button(root, text="Z--", command=VZsm)).grid(row=100 + 4, column= 100 + 3)
    (Button(root, text="XY+", command=XYp)).grid(row=100 + 1, column= 100 + 4)
    (Button(root, text="XY-", command=XYm)).grid(row=100 + 2, column= 100 + 4)
    (Button(root, text="XY++", command=XYsp)).grid(row=100 + 3, column= 100 + 4)
    (Button(root, text="XY--", command=XYsm)).grid(row=100 + 4, column= 100 + 4)
    (Button(root, text="XZ+", command=XZp)).grid(row=100 + 1, column= 100 + 5)
    (Button(root, text="XZ-", command=XZm)).grid(row=100 + 2, column= 100 + 5)
    (Button(root, text="XZ++", command=XZsp)).grid(row=100 + 3, column= 100 + 5)
    (Button(root, text="XZ--", command=XZsm)).grid(row=100 + 4, column= 100 + 5)
    (Button(root, text="YZ+", command=YZp)).grid(row=100 + 1, column= 100 + 6)
    (Button(root, text="YZ-", command=YZm)).grid(row=100 + 2, column= 100 + 6)
    (Button(root, text="YZ++", command=YZsp)).grid(row=100 + 3, column= 100 + 6)
    (Button(root, text="YZ--", command=YZsm)).grid(row=100 + 4, column= 100 + 6)












            
            
    
    
    
    




    
    
