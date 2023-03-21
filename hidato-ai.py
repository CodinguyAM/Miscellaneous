from math import floor

def displayPath(path):
  #print("PATH")
  for staten in range(len(path)):
    state = path[staten]
    #print("State No.", staten, ":")
    #displayBoard(state[0])
    #print("WASPLACING:", state[1])
    #print("WASLOC:", state[2], state[3])
def tuplify(board):
  r = []
  for row in board:
    r.append(tuple(row))
  return tuple(r)

def listify(board):
  r = []
  for row in board:
    r.append(list(row))
  return r
#parse board string

def parseBoardString(boardString):
  #init board to an empty list
  board = []
  #create list of rows (rows in bs seperated by commas)
  rowlist = boardString.split(",")

  #add top border
  board.append(["."]*(len(rowlist[0].split("|"))))

  #go through every row
  for row in rowlist:
    #get individual cells
    cellist = row.split("|")

    #left and right borders
    for i in range(len(cellist)):
      if cellist[i] == "":
        cellist[i] = "."
      #convert filled cells to ints
      try:
        cellist[i] = int(cellist[i])
      except:
        pass
    #append the list version of the row (cellist) to the board
    board.append(cellist)

  #bottom border
  board.append(["."]*(len(rowlist[0].split("|"))))
  return board

def displayBoard(board):
  for row in board:
    for cell in row:
      cellstr = str(cell)
      print(cellstr, end=" "*(3 - len(cellstr)))
    print()
  print()

def firstLoc(board):
  for rownum in range(len(board)):
    row = board[rownum]
    for cellnum in range(len(row)):
      cell = row[cellnum]
      if cell == 1:
        return (cellnum, rownum)

def endLoc(board):
  maxc = 0
  for rownum in range(len(board)):
    row = board[rownum]
    for cellnum in range(len(row)):
      cell = row[cellnum]
      try:
        if cell > maxc:
          maxc = cell
      except:
        pass
  return maxc

def preNumLocFinder(board):
  r = {}
  
  for rownum in range(len(board)):
    row = board[rownum]
    for cellnum in range(len(row)):
      cell = row[cellnum]
      if (cell != ".") and (cell != "!"):
        r[cell] = (cellnum, rownum)

  return r
def nextstate(board, placing, pointerX, pointerY, preNumLocs, visitsDict, path, maxc):
  #displayBoard(board)
  #A state is a tuple of (board, placing, pointerX, pointerY, visitsDict, path)
  #print(list(preNumLocs.keys()))
  #shorten pointerX and pointerY to just x and y
  x = pointerX
  y = pointerY
  #print("LOC: ", x, y)
  #print("PLACING: ", placing)
  displayPath(path)
  #tuplify board
  tup_board = tuplify(board)
  #get neighbours
  neighbs = [(y-1,x),(y-1,x+1),(y,x+1),(y+1,x+1),(y+1,x),(y+1,x-1),(y,x-1),(y-1,x-1)]
  #             N        NE      E       SE       S           SW       W      NW
  #empty neighbours
  emptyNeighbs = []
  for neighb in neighbs:
    #print("NEIGHB: ", neighb[1], neighb[0], 'VAL:', board[neighb[0]][neighb[1]])
    
    #print(len(board), neighb[0])
    #print(len(board[neighb[0]]), neighb[1])
    if board[neighb[0]][neighb[1]] == "!":
      emptyNeighbs.append(neighb)
  #print(emptyNeighbs)
  visreq = len(emptyNeighbs)
  vdk = (x, y, placing, tup_board)
  visits = visitsDict.get(vdk, 0)
  
  #We want to place a number already pre-filled on the board
  
  if placing in preNumLocs.keys():
    #print("placing prenum")
    if visits == visreq + 1:
      #move back
      board, placing, x, y = path.pop()
      board = listify(board)
      
      #return vals
      return (listify(board), placing, x, y, visitsDict, path)

    #we can go to it
    if preNumLocs[placing][::-1] in neighbs:
      #print("GO")
      #blacklist if we ever need to come back
      visitsDict[vdk] = visreq + 1

      #add to path
      path.append((tuplify(board), placing, x, y))

      #return vals
      return (listify(board), placing + 1, preNumLocs[placing][0], preNumLocs[placing][1], visitsDict, path)

    #we cannot go to it
    else:
      #print("CG")
      #blacklist current loc
      visitsDict[vdk] = visreq

      #move back
      board, placing, x, y = path.pop()
      board = listify(board)

      #return vals
      return (listify(board), placing, x, y, visitsDict, path)

    
  else:
    if visits == visreq:
      #move back
      board, placing, x, y = path.pop()
      board = listify(board)
      #return vals
      return (board, placing, x, y, visitsDict, path)
    
    path.append((tuplify(board), placing, x, y))
    
    #move pointer to spot
    y, x = emptyNeighbs[visits]

    board[y][x] = placing
    
    #we've visited!
    visitsDict[vdk] = visits + 1

    #return pointer
    return (listify(board), placing + 1, x, y, visitsDict, path)
      
def AI(boardString):
  board = parseBoardString(boardString)
  #displayBoard(board)
  pointerX, pointerY = firstLoc(board)
  preNumLocs = preNumLocFinder(board)
  visitsDict = {}
  path = []
  #print(pointerX, pointerY)
  #print(preNumLocs)
  N = 2
  steps = 0
  while N <= endLoc(board):
    board, N, pointerX, pointerY, visitsDict, path = nextstate(board, N, pointerX, pointerY, preNumLocs, visitsDict, path, endLoc(board))
    steps = steps + 1
  print("Difficulty:", floor(10 * steps/(endLoc(board)))/10)
  print("Steps Taken:", steps)
  return board

print("Advay's Hidato AI!")
print()
print('''The game Hidato is from The Economic Times (of India). The board of Hidato consists of a grid of squares, and may be in any shape. Hidato board shapes are generally symmetric. Certain squares in the board are pre-marked with numbers. The objective of the game is to find a path of consecutive numbers from one to the maximum, connecting these horizontally, vertically, or diagonally. This is acheived by placing numbers to fill in whatever empty spots are on the grid.''')
print()
print("To generate boardstrings, visit: https://boardgenhai-aux.advaymisra2.repl.co/")
print()
print('''This AI finds the solution by using a depth-first search algorithm. It's not the smartest AI, but it's pretty good. However, it does like moving up.''')
print()
while True:
  try:
    bs = input("Enter boardstring: ")
    displayBoard(parseBoardString(bs))
    displayBoard(AI(bs))
    print()
    print()
    print()
  except:
    print("No Solution!")
    continue
