class Vector:
    def __init__(self, *comps):
        comp2 = []
        for c in comps:
            if type(c) in (type(0), type(0.0)):
                comp2.append(c)
            if type(c) in (type(()), type([])):
                comp2.extend(c)
        comps = comp2
        self.dimension = len(comps)
        self.d = self.dimension
        self.dim = self.d
        self.comps = list(comps)

    def __repr__(self):
        return '(' + ' '.join(self.comps) + ')'

    def __add__(self, other):
        other = Vector(other)
        if other.d != self.d:
            raise ValueError
        else:
            r = []
            for x in range(self.d):
                r.append(self.comps[x] + other.comps[x])
            return Vector(r)

    def __mult__(self, other):
        if type(other) == type(0):
            r = []
            for x in range(self.d):
                r.append(self.comps[x] * other)
            return Vector(r)
        else:
            other = Vector(other)
            
