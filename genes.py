import random

pmult = 0.1
mults = [

class Animal:
    def __init__(self, genome):
        self.c1 = genome[0]
        self.c2 = genome[1]
        self.chr = len(genome[0])
    def phen(self):
        r = []
        for x in range(self.chr):
            g1 = self.c1[x]
            g2 = self.c2[x]
            if (g1[1], g2[1]) == ('N', 'N'):
                r = r + [max((g1[0], g2[0]))]
            elif (g1[1], g2[1]) in (('N', 'M'), ('M', 'N')):
                r = r + [g1[1] * g2[1]]
            elif (g1[1], g2[1]) == ('M', 'M'):
                r = r + [1]
        return r
    def cr(self):
        r = []
        for x in range(self.chr):
            if random.random() < 0.5:
                r = r + self.c1[x]
            else:
                r = r + self.c2[x]
        return r
    def score(self):
        return sum(self.phen())/self.chr
    def baby(self, other):
        return Animal([self.cr, other.cr])


def eveolve(generation):
    scores = [x.score() for x in generation]
    aps = sum(scores)/len(scores)
    surv = [x for x in generation if x.score > aps]
    r = []
    for x in range(len(surv) // 2):
        r.append(surv[x*2].baby(surv[1+x*2]))
    return r

def genrand():
    
                 
        
            
                
