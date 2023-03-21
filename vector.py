import math as trig

def toRect(r, theta):
    t = trig.radians(theta)
    return (r*trig.cos(t), r*trig.sin(t))

def toMagn(x, mag):
    return int(x*10**mag)/10**mag

def toPolar(x, y):
    mag = (x**2+y**2)**(1/2)
    t = toMagn(trig.acos(x/mag), 7)
    #print(t)
    t2 = toMagn(trig.asin(y/mag), 7)
    #print(t2)
    if t == t2:
        return (mag, trig.degrees(t))
    else:
        print("YUP, THIS THING IS BROKEN.")

#toPolar(1, 2)

class Vector:
    def __init__(self, x, y):
        self.rects = (x, y)
        self.x = x
        self.y = y
        self.polars = toPolar(x, y)
        self.r = self.polars[0]
        self.theta = self.polars[1]
        self.mag = self.r
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def mult(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


#print(toPolar(100, 12))
