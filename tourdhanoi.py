from math import inf

def checkLegal(move, board):
    s = int(move[0])
    f = int(move[1])
    sPole = board[s]
    fPole = board[f]
    sIndex = -1
    fIndex = -1
    for sd in sPole:
        if sd != 0:
            sDisk = sd
            sIndex = sIndex + 1
    if sIndex == -1:
        return "ivm"
    for fd in fPole:
        if fd != 0:
            fDisk = fd
            fIndex= fIndex + 1
    if fIndex == -1:
        fDisk = inf
    if sDisk > fDisk:
        return "ivm"
    else:
        sPole[sIndex] = 0
        fPole[fIndex + 1] = sDisk
    board[s] = sPole
    board[f] = fPole
    return board

def checkWin(board, level):
    return list(range(1, level + 1))[::-1] in board[1:]
def boardGen(numDiscs):
    return [list(range(1, numDiscs + 1))[::-1], [0] * numDiscs, [0] * numDiscs]

def disp(board):
    lines = [""] * len(board[0])
    #print(lines)
    maxLen = 0
    for n in board[0]:
        if len(str(n)) > maxLen:
            maxLen = len(str(n))
    for n in board[1]:
        if len(str(n)) > maxLen:
            maxLen = len(str(n))
    for n in board[2]:
        if len(str(n)) > maxLen:
            maxLen = len(str(n))

    #print(maxLen)      
    for r in range(len(board[0])):
        if board[0][r] != 0:
            lines[r] = lines[r] + str(board[0][r]) + " " * (maxLen - len(str(board[0][r])) + 1)
        else:
            lines[r] = lines[r] + "." + " " * (maxLen - len(str(board[0][r])) + 1)
    
    
    for r in range(len(board[1])):
        if board[1][r] != 0:
            lines[r] = lines[r] + str(board[1][r]) + " " * (maxLen - len(str(board[1][r])) + 1)
        else:
            lines[r] = lines[r] +  "." + " " * (maxLen - len(str(board[1][r])) + 1)

    
    for r in range(len(board[2])):
        if board[2][r] != 0:
            lines[r] = lines[r] + str(board[2][r]) + " " * (maxLen - len(str(board[2][r])) + 1)
        else:
            lines[r] = lines[r] + "." + " " * (maxLen - len(str(board[2][r])) + 1)

    for line in lines[::-1]:
        print(line)
    print()
level = 0             
while True:                
    level = level + 1
    print(str(level) + "-disc Tower of Hanoi")
    board = boardGen(level)
    disp(board)
    moves = 0
    while not (checkWin(board, level) and moves > 0):
        move = input("Move?: ")
        nboard = checkLegal(move, board)
        if type(nboard) != type(""):
            board = nboard
            moves = moves + 1
            disp(board)
        else:
            print("Illegal Move.")

    print("You solved a", str(level) + "-disc Tower of Hanoi in", moves, "moves")
    print()
