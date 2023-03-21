import tkinter as tk

def olb(board):
  r = []
  for row in board:
    r.extend(row)
  return r

def dispBoard(board):
  global bunchobuttons
  bob = bunchobuttons
  ob = olb(board)
  for x in range(187):
    if x % 11 == 0:
      print()
    if ob[x] not in [".", "|"]:
      bob[x]["text"] = ob[x]
      print(ob[x], end=" ")
    else:
      print(" ", end=" ")
      bob[x]["text"] = " "


def adj(board, x, y):
  r = {}
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      np = (x + dx, y + dy)
      if (dx, dy) == (0, 0):
        continue
      else:
        r[np] = board[np[1]][np[0]]
  return r
  

def performMove(mf, mt, board, move):
  ''' mf is a string/list/tuple of [y, x] form for where  the piece being moved is. mt is the same, but it describes the piece's destination. board is the current board. move is whose move it is 0 -> lowercase, 1 -> uppercase.'''
  mfy = int(mf[0])
  mfx = int(mf[1])
  piece = board[mfy][mfx]
  mty = int(mt[0])
  mtx = int(mt[1])
  dest_piece = board[mty][mtx]
  adj_pcs = list(adj(board, mfx, mfy).values())
  if piece in [".", "|"]:
    return "Moving a board square would be strange."
  if move == 0 and piece == piece.upper():
    return "Lower is trying to move an upper piece"
  if move == 1 and piece == piece.lower():
    return "Upper is trying to move a lower piece"
  if move == 1 and dest_piece == dest_piece.upper() and not dest_piece == ".":
    return "Upper is taking their own piece"
  if move == 0 and dest_piece == dest_piece.lower() and not dest_piece == ".":
    return "Lower is taking their own piece"
  if piece.upper() == "D":
    #Duke code
    #If squre is not adjacent
    if (mtx, mty) not in adj(board, mfx, mfy).keys():
      #duke not allowed
      return "Duke is trying to move to inadj square"
    
    if adj_pcs.count('K') + adj_pcs.count("k") >= 1:
      #duke can go any adj with king near
      board[mfy][mfx] = "."
      board[mty][mtx] = piece
      
      return board
    if adj_pcs.count('B') + adj_pcs.count('b') >= 1:
      #duke can go any diag adj with countess near
      if (mtx, mty) not in [(mfx + 1, mfy + 1), (mfx - 1, mfy + 1), (mfx + 1, mfy - 1), (mfx -1, mfy - 1)]:
        return "Duke with countess power is trying to move to indiag adj square"
      else:
        board[mfy][mfx] = "."
        board[mty][mtx] = piece
        return board
    if adj_pcs.count('C') + adj_pcs.count('c') >= 1:
      #duke can go any hv adj with count near
      if (mtx, mty) not in [(mfx, mfy + 1), (mfx - 1, mfy), (mfx, mfy - 1), (mfx + 1, mfy)]:
        return "Duke with count power is trying to move to inhv adj square"
      else:
        board[mfy][mfx] = "."
        board[mty][mtx] = piece
        return board
    if move == 1:
      #normal duke movement.
      if (mtx, mty) not in [(mfx + 1, mfy + 1), (mfx - 1, mfy + 1)]:
        return "Powerless duke cannot move much"
      else:
        board[mfy][mfx] = "."
        board[mty][mtx] = "D"
        return board
    elif  move == 0:
      if (mtx, mty) not in [(mfx + 1, mfy - 1), (mfx - 1, mfy - 1)]:
        return "Powerless due cannot move much"
      else:
        board[mfy][mfx] = "."
        board[mty][mtx] = "d"
        return board
  
  elif piece.upper() == "L":
    if (mtx, mty) in adj(board, mfx, mfy):
      return "Lord can not move to adj squares"
    if (not ((abs(mfx - mtx) == 0) or (abs(mfy - mty) == 0))) or (mtx, mty) in adj(board, mfx, mfy).keys():
      #if not hv
      return "Lord can only move hv"
    #cant drive over a broken bridge. checks to see for gaps
    #vertically
    if abs(mfx - mtx) == 0:
      isl = True
      for y in range(mfy, mty):
        if board[y][mfx] == ".":
          isl = False
      if isl:
        board[mfy][mfx] = "."
        board[mty][mtx] = piece
        return board
      else:
        return "Gaps in vertical bridge"
    #horizontally
    if abs(mfy - mty) == 0:
      isl = True
      for x in range(mfx, mtx):
        if board[mfy][x] == ".":
          isl = False
      if isl:
        board[mfy][mfx] = "."
        board[mty][mtx] = piece
        return board
      else:
        return "Gaps in horizontal bridge"
  elif piece.upper() == "C":
    if (not ((abs(mfx - mtx) == 0) or (abs(mfy - mty) == 0))):
      #if not hv
      if abs(mtx - mfx) == 2 and abs(mty - mfy) == 2:
        board[mfy][mfx] = "."
        board[mty][mtx] = piece
        return board
      return "Count can only move hv"
    else:
      if abs(mfy - mty) == 0:
        isl = True
        for x in range(mfx + int((mtx - mfx)/abs(mtx - mfx)), mtx):
          if board[mfy][x] != ".":
            isl = False
        if isl:
          board[mfy][mfx] = "."
          board[mty][mtx] = piece
          return board
        else:
          return "Count is tryingto jump vertically"
      if abs(mfx - mtx) == 0:
        isl = True
        for y in range(mfy + int((mty - mfy)/abs(mty - mfy)), mty):
          if board[y][mfx] != ".":
            isl = False
        if isl:
          board[mfy][mfx] = "."
          board[mty][mtx] = piece
          return board
        else:
          return "Count is tryingto jump horizontally"
  elif piece.upper() == "B":
    if not (abs(mfx - mtx) == abs(mfy - mty)):
      #if not diag
      if (abs(mtx - mfx) == 2 or abs(mty - mfy) == 2) and not (abs(mtx - mfx) == 2 and abs(mty - mfy) == 2):
        board[mfy][mfx] = "."
        board[mty][mtx] = piece
        return board
      return "Countess can only move diagonally"
    else:
      isl = True
      n = 0
      for x in range(mfx + int((mtx - mfx)/abs(mtx - mfx)), mtx):
        if board[mfy + n][x] != ".":
          isl = False
        n = n + 1
      if isl:
        board[mfy][mfx] = "."
        board[mty][mtx] = piece
        return board
      else:
        return "Countess cannot jump"
  elif piece.upper() == "K":
    if not ((( ((abs(mfx - mtx) == 0) or (abs(mfy - mty) == 0)))) or ((abs(mfx - mtx) == abs(mfy - mty)))):
      return "Even a king can only move hvd."
    else:
      if abs(mfy - mty) == 0:
        isl = True
        for x in range(mfx + int((mtx - mfx)/abs(mtx - mfx)), mtx):
          if board[mfy][x] != ".":
            isl = False
        if isl:
          board[mfy][mfx] = "."
          board[mty][mtx] = piece
          return board
        else:
          return "Kings cant do acrobatics! h"
      if abs(mfx - mtx) == 0:
        isl = True
        for y in range(mfy + int((mty - mfy)/abs(mty - mfy)), mty):
          if board[y][mfx] != ".":
            isl = False
        if isl:
          board[mfy][mfx] = "."
          board[mty][mtx] = piece
          return board
        else:
          return "Kings cant do acrobatics! v"
      else:
        isl = True
        n = 0
        for x in range(mfx + int((mtx - mfx)/abs(mtx - mfx)), mtx):
          if board[mfy + n][x] != ".":
            isl = False
          n = n + int((mtx - mfx)/abs(mtx - mfx))
        if isl:
          board[mfy][mfx] = "."
          board[mty][mtx] = piece
          return board
        else:
          return "Kings cant do acrobatics! d"
  else:
    return "Upper, its a BOARD SQUARE, not a piece!"
      
      
board = [["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
         ["|", "D", "L", "C", "B", "F", "B", "C", "L", "D", "|"],
         ["|", "D", "L", "C", "B", "K", "B", "C", "L", "D", "|"],
         ["|", "D", "D", "D", "D", "D", "D", "D", "D", "D", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
         ["|", "d", "d", "d", "d", "d", "d", "d", "d", "d", "|"],
         ["|", "d", "l", "c", "b", "k", "b", "c", "l", "d", "|"],
         ["|", "d", "l", "c", "b", "f", "b", "c", "l", "d", "|"],
         ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]]

mf = (0, 0)
mt = (0, 0)
partway = 0
move = 1
winner = 3
def whenclicked(bx, by):
  global mf, mt, partway, move, board, playerText, winner
  if winner == 3:
    if move == 1:
      playerText['text'] = "Player 1's Turn"
    else:
      playerText["text"] = "Player 2's Turn"
    if partway == 0:
      mf = (by, bx)
      partway = 1
    if partway == 1 and mf != (by, bx):
      mt = (by, bx)
      nboard = performMove(mf, mt, board, move)
      if type(nboard) != type(""):
        board = nboard
        dispBoard(board)
        
        move = (move + 1) % 2
      else:
        print(nboard)
      partway=0
    if move == 1:
      playerText['text'] = "Player 1's Turn"
    else:
      playerText["text"] = "Player 2's Turn"
      
  ob = olb(board)
  if ob.count('f') == 0:
    playerText["text"] = "Player 1 Wins!"
    winner = 1
  elif ob.count('F') == 0:
    playerText["text"] = "Player 2 Wins!"
    winner = 2
  
root = tk.Tk()
#x into y
cwidth = 4
cheight = 2
root.geometry("400x640")
selectedSquare = "none"
bunchobuttons = []
for x in range(187):
  if x % 11 in [0, 10]:
    exec('def ril' + str(x) + '(): \n  whenclicked(' + str(x % 11) + ', ' + str((x - (x % 11))/11) + ')\napbut = tk.Button(root, text="", background="black", width = ' + str(cwidth) + ', height = ' + str(cheight) + ', command=ril' + str(x) + ')')
  elif (x - (x % 11))/11 in [0, 16]:
    exec('def ril' + str(x) + '(): \n  whenclicked(' + str(x % 11) + ', ' + str((x - (x % 11))/11) + ')\napbut = tk.Button(root, text="", background="black", width = ' + str(cwidth) + ', height = ' + str(cheight) + ', command=ril' + str(x) + ')')
  elif (x % 2 == 0):
    exec('def ril' + str(x) + '(): \n  whenclicked(' + str(x % 11) + ', ' + str((x - (x % 11))/11) + ')\napbut = tk.Button(root, text="", background="pink" , width = ' + str(cwidth) + ', height = ' + str(cheight) + ', command=ril' + str(x) + ')')
  else:
    exec('def ril' + str(x) + '(): \n  whenclicked(' + str(x % 11) + ', ' + str((x - (x % 11))/11) + ')\napbut = tk.Button(root, text="", background="brown", width = ' + str(cwidth) + ', height = ' + str(cheight) + ', command=ril' + str(x) + ')')
  bunchobuttons.append(apbut)

for x in range(187):
  but = bunchobuttons[x]
  but.grid(row=int((x - (x % 11))/11), column = x % 11, sticky="NESW")

playerText = tk.Label(root, text="Player 1's Turn")
playerText.grid(row = 18, column = 4, columnspan = 3)
dispBoard(board)
tk.mainloop()
    
