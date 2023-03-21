MAINBOARD = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
BigBoard = [[MAINBOARD, MAINBOARD, MAINBOARD], [MAINBOARD, MAINBOARD, MAINBOARD], [MAINBOARD, MAINBOARD, MAINBOARD]]

def display(board):
    for bigrow in board:
        for minib in bigrow:
            for minirow in minib:
                pr = ""
                for sq in minirow:
                    pr = pr + sq
                print(pr)
            print("___")
        print()

def at(LOC, board):
    return board[LOC[0]][LOC[1]][LOC[2]][LOC[3]]

def replace(LOC, board, replacer):
    board[LOC[0]][LOC[1]][LOC[2]][LOC[3]] = replacer
    return board

print()
display(replace([0, 0, 0, 0], BigBoard, "X"))
