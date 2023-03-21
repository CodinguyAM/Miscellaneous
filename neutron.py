import tkinter as tk

n = []
for x in [-1, 0, 1]:
  for y in [-1, 0, 1]:
    if (x, y) != (0, 0):
      n.append([x, y])


def at(board, y, x):
  if y < len(board) and y >= 0:
    if x < len(board[y]) and x >= 0:
      return board[y][x]
    else:
      return False
  else:
    return False


def possQueenMoves(board):
  r = []
  n = []
  for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
      if (x, y) != (0, 0):
        n.append([x, y])
  n.remove([x, y])
  print(n)
  for x in range(len(board[0])):
    for y in range(len(board)):
      if at(board, y, x) in 'aA':

        for dx, dy in n:
          nx = x + dx
          ny = y + dy
          print(at(board, ny, nx), nx, ny, x, y, dx, dy, 'TENTAT')
          if at(board, ny, nx) == '.':
            while at(board, ny, nx) == '.':
              print(at(board, ny, nx), nx, ny, x, y, dx, dy, 'SOFAR')
              nx = nx + dx
              ny = ny + dy
            r.append([[x,y],[nx-dx,ny-dy]])
  return r


def isValQueenMove(board, f, t, move):

  return [f, t] in possQueenMoves(board) and {
    0: 'a',
    1: 'A'
  }[move % 2] == at(board, f[1], f[0])


def possNeutronMoves(board):
  r = []
  n = []
  for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
      if (x, y) != (0, 0):
        n.append([x, y])
  n.remove([x, y])
  for x in range(len(board[0])):
    for y in range(len(board)):
      if board[y][x] == 'N':
        for dx, dy in n:
          nx = x + dx
          ny = y + dy
          if at(board, ny, nx) == '.':
            r.append([[x,y],[nx-dx,ny-dy]])
  return r


def isValNeutMove(board, f, t, move):
  return [f, t] in possNeutronMoves(board)


def dispBoard(board,h=1,w=2):
  root = tk.Tk()
  for x in range(len(board[0])):
    for y in range(len(board)):
      b = tk.Button(root,
                    bg={
                      'a': 'red',
                      'A': 'blue',
                      '.': 'white',
                      'N': 'grey'
                    }[board[y][x]],
                    command=lambda x=x, y=y: wc(x, y),
                    height=h,
                    width=w)
      b.grid(row=y, column=x)
  return root


board = []
s = 5
board.append(['a'] * s)
for n in range(s - 2):
  board.append(['.'] * s)
board.append(['A'] * s)
board[int(s / 2)][int(s / 2)] = 'N'
p = False
turn = 'queen'
move = 0
rooty = dispBoard(board)


def wc(bx, by):
  global rooty, board, f, t, turn, move, p
  if turn == 'queen':
    if not p:
      f = [bx, by]
      p = True
    else:
      t = [bx, by]
      if isValQueenMove(board, f, t, move):
        rooty.destroy()
        board[f[1]][f[0]] = '.'
        board[t[1]][t[0]] = {0: 'a', 1: 'A'}[move % 2]
        rooty = dispBoard(board)
        p = False
        turn = 'neutron'
      else:
        print([f, t])
        print(possQueenMoves(board))
        print('ILLEG')

  if turn == 'neutron':
    if not p:
      f = [bx, by]
      p = True
    else:
      t = [bx, by]
      if isValNeutMove(board, f, t, move):
        rooty.destroy()
        board[f[1]][f[0]] = '.'
        board[t[1]][t[0]] = 'N'
        rooty = dispBoard(board)
        p = False
        move = move + 1
        turn = 'queen'
      else:
        print([f, t])
        print(possNeutronMoves(board))
        print('ILLEG')
