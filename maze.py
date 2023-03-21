#raise SyntaxError
def validI(x):
    return range(len(x))
class Maze:
    def __init__(self, mazeText):
        self.maze = []
        for row in mazeText.split(sep=" "):
            a = []
            for char in row:
                a.append(char)
            self.maze.append(a)
        self.fLoc = None
        self.startLoc = None
        for iR in validI(self.maze):
            R = self.maze[iR]
            for iC in validI(R):
                C = R[iC]
                if C == "0":
                    self.fLoc = (iC, iR)
                elif C == "@":
                    self.startLoc = (iC, iR)
                else:
                    continue
        self.costs = self.maze


        #completely unnecessary functions that needs to be defined in here
        def at(loc):
            x, y = loc
            return self.maze[y][x]
        def Eat(ls, loc):
            x, y = loc
            return ls[y][x]
        def isIn(loc):
            si = False
            try:
                at(loc)
                si = True
            except:
                si = False
            return si
        def EisIn(loc):
            si = False
            try:
                Eat(ls, loc)
                si = True
            except:
                si = False
            return si
        def neighbs(loc):
            x = loc[0]
            y = loc[1]
            retur =  [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for z in retur:
                if not isIn(z) or (at(z) != "." and not (at(z) == "G" or at(z) == "@")):
                    retur.remove(z)
            return retur
        def Eneighbs(ls, loc):
            x = loc[0]
            y = loc[1]
            retur =  [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for z in retur:
                if not EisIn(ls, z) or (Eat(ls, z) != "." and not (Eat(ls, z) == "G" or Eat(ls, z) == "@")):
                    retur.remove(z)
            return retur
        def doCosts(mazeObj):
            MAZE = mazeObj.maze
            FLOC = mazeObj.fLoc
            mazeObj.costs[FLOC[1]][FLOC[0]] = 0
            curInd = 0
            for n in range(2 ** len(MAZE)):
                locs = []
                for iR in validI(MAZE):
                    for iC in validI(MAZE[iR]):
                        if Eat(mazeObj.costs, (iC, iR)) == curInd:
                            locs.extend(Eneighbs(mazeObj.costs, (iC, iR)))
                for loc in locs:
                    mazeObj.costs[loc[1]][loc[0]] = curInd + 1
                curInd = curInd + 1
        self.neighbs = lambda loc: neighbs(loc)
        self.costs = doCosts(self)
        self.traversed = self.maze
        self.cr = fLoc[1]
        self.cc = fLoc[0]
        for iR in validI(self.maze):
            R = self.maze[iR]
            a = []
            for iC in validI(R):
                C = R[iC]
                if C == "@":
                    a.append("P")
                else:
                    a.append(at((iR, iC)))
            self.traversed.append(a)
    def move(self):
        print(dd)
    
