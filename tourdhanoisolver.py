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

def boardGen(numDiscs):
    return [list(range(1, numDiscs + 1))[::-1], [0] * numDiscs, [0] * numDiscs]

def holderPole(s, f):
    return {(0, 1):2, (0, 2):1, (1, 0):2, (1, 2):0, (2, 0):1, (2, 1):0}[(s, f)]

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


def RHA(discs, s, f):
    if discs == 1:
        return [str(s) + str(f)]
    else:
        h = holderPole(s, f)
        return RHA(discs - 1, s, h) + [str(s) + str(f)] + RHA(discs - 1, h, f)

discs = 1
while True:
    print("For", discs, "discs, the instuction manual is: ")
    solution = RHA(discs, 0, 2)
    board = boardGen(discs)
    for s in solution:
        disp(board)
        board = checkLegal(s, board)
        print()
        print()
    disp(board)
    print()
    print()
    print("-----------------------------------END OF INSTRUCTION MANUAL FOR", discs, "DISCS-------------------------------------------")
    print("\n" * 4)
    discs = discs + 1

