from math import inf

def o1l(m):
    r = []
    for o in m:
        for e in o:
            r.append(e)
    return r

def properFormat(maze):
    r = []
    r.append(["|"] * (len(maze[0])+2))
    for row in maze:
        r.append(["|"] + row + ["|"])
    r.append(["|"] * (len(maze[0])+ 2))
    return r

def dispMaze(maze):
    maxLen = len(str(max(o1l(maze), key=lambda x: len(str(x))))) + 1
    #r = 0
    for row in maze:
        #c = 0
        for cell in row:
            if cell == "|":
                cell = "."
            elif cell == ".":
                cell = " "
            elif cell == inf:
                cell = "."
            else:
                pass
            print(cell, end=" "*(maxLen - len(str(cell))))
            #c = c + 1
        print()
        #r = r + 1

def assignCosts(maze):
    maze=maze[:]
    #dispMaze(maze)
    #print(maze)
    #maze = properFormat(maze)
    #print(maze)
    costs = []
    for y in range(len(maze)):
        a = []
        #print(maze[y])
        for x in maze[y]:
            if x in ".@":
                a.append(inf)
                #print("I", end="")
            elif x == "G":
                a.append(0)
                #print("O", end="")
            else:
                a.append(-2)
                #print("M", end="")
        #print()
        #print(a)
        costs.append(a)
    #dispMaze((costs))
    #print("\n" * 2)
    #print(o1l(costs).count(inf))
    
    while o1l(costs).count(inf) > 0:
        #print()
        for x in range(1, len(costs[0]) - 1):
            for y in range(1, len(costs) -1):
                #dispMaze(costs)
                #print("\n" * 2)
                #print(x, y)
                #print([(x,y-1),(x+1,y),(x,y+1),(x-1,y)])
                #print(costs[y][x])
                if costs[y][x] > -2:
                    for way in [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]:
                        if costs[way[1]][way[0]] >= costs[y][x]:
                            #dispMaze(costs)
                            costs[way[1]][way[0]] = costs[y][x] + 1
    for y in range(len(costs)):
        for x in range(len(costs[y])):
            if costs[y][x] == -2:
                costs[y][x] = inf
    return costs


def adj(t):
    x = t[0]
    y = t[1]
    return [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]


def nextStep(costs, traveller):
    return min(adj(traveller), key=lambda t:costs[t[1]][t[0]])

def solve(maze):
    maze = properFormat(maze)
    costs = assignCosts(maze)
    solution = maze[:]
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "@":
                pos = (x, y)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "G":
                goal = (x, y)
    while pos != goal:
        if solution[pos[1]][pos[0]] != "@":
            solution[pos[1]][pos[0]] = ")"
        pos = nextStep(costs, pos)
        
    return solution
    


##testMaze = [[".", "G", "."],
##            [".", "|", "."],
##            [".", "@", "."]]

fhand = open("zmaze.txt", mode="r")
m = fhand.read()
mazeRows = m.split("\n")
#print(mazeRows)
testMaze = []
for row in mazeRows:
    testMaze.append(list(row))


testMaze = properFormat(testMaze)
#dispMaze(testMaze)
dispMaze(properFormat(testMaze))
print("\n"*3)
dispMaze(assignCosts(testMaze))
print("\n" * 3)
dispMaze(solve(testMaze))

                
                
                
