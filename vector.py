class Vector:
    def __init__(self,*args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1:
            a = args[0]
            if type(a) == type(Vector(0, 1)):
                self.x = a.x
                self.y = a.y
            else:
                self.x = args[0][0]
                self.y = args[0][1]

    def __add__(self, vector2):
        vector2 = Vector(vector2)
        nx = self.x + vector2.x
        ny = self.y + vector2.y
        return Vector(nx, ny)

    def scalarMultiply(self, n):
        nx = self.x * n
        ny = self.y * n
        return Vector(nx, ny)

    def __mul__(self, o):
        if type(o) == type(0):
            return Vector.scalarMultiply(self, o)
        elif type(o) == type(Vector(0,1)):
            return Vector.dotProduct(self, o)
    def __sub__(self, vector2):
        return self + ( vector2 * -1)

    def dotProduct(self, vector2):
        x1 = self.x
        y1 = self.y
        x2 = vector2.x
        y2 = vector2.y
        return (x1 * x2) + (y1 * y2)

    def __repr__(self):
        return str(self.x) + ' ' + str(self.y)

    def magn(self):
        return (((self.x) ** 2) + ((self.y) ** 2)) ** (1/2)
a = Vector(7, 3)
b = Vector([4,3])
c = Vector(b)
print(a)
print(b)
print()
print(a + b)
print(b + a)
print(a * 2)
print(a * b)
print(a - b)
print(b - a)
print(b.magn())
    
    
