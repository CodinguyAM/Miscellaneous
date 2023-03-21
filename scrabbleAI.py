from itertools import permutations as orders

words = open("scrabbleWords2.txt").read().split(', ')+open("scrabbleWords.txt").read().split(', ')
print(len(words), "words loaded.")
#print(type(WORDS))
def genPrefixes(words):
    r = set([])
    for word in words[::-1]:
        if word not in r:
            for x in range(len(word) - 1):
                r = r | {word[:x]}
    return list(r)
#print(genPrefixes(words))
try:
    prefixes = open('prefixes.txt').read().split(', ')
except:
    phandle = open('prefixes.txt', 'w')
    phandle.write(', '.join(genPrefixes(words)))
    phandle.close()

print(len(prefixes), "prefixes loaded.")
def allinrow(p):
    rown = p[0][1]
    for o in p:
        if o[1] !=rown:
            return False
    return True

def allincol(p):
    coln = p[0][0]
    for o in p:
        if o[0] !=coln:
            return False
    return True



def isValid(board, playedon, rack):
    global words
    tilesplayed = []
    for p in playedon:
        tilesplayed.append(board[p[1]][p[0]])
    for t in tilesplayed:
        if tilesplayed.count(t) > rack.count(t):
            return False
    if not(allincol(playedon) or allinrow(playedon)):
        return False
    if allinrow(playedon):
        y = playedon[1]
        mainword = ''
        for x in range(min(playedon, key=lambda a:a[0]), max(playedon, key=lambda a:a[0])+1):
            
        for x in range(min(playedon, key=lambda a:a[0]), max(playedon, key=lambda a:a[0])+1):
            #check for cross-words!
            cw = ''
            ny = y
            nny = ny + 1
            while board[ny][x] not in '.|':
                cw = board[ny][x] + cw
                ny = ny - 1
            while board[nny][x] not in '.|':
                cw = cw + board[nny][x]
                nny = nny + 1
            if len(cw) > 1 and cw not in words:
                return False
    
