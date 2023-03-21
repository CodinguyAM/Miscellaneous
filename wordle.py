import random

def randchoose(ls):
    return ls[random.randint(0, len(ls)-1)]

HANDLE = open('zwords.txt')
words = HANDLE.read().split(', ')
HANDLE.close()
#print(words)
print(len(words), "words loaded...")
def evalinp(inp, word):
    rs = ""
    for index in range(len(word)):
        letter = word[index]
        inpletter = inp[index]
        if inpletter == letter:
            rs = rs + "G"
        elif inpletter in word:
            rs = rs + "Y"
        elif inpletter not in word:
            rs = rs + "B"
    return rs

#print(evalinp("MOIST", "MOUTH"))
print("This is a Python implementation of the game Wordle by James Wardle.")
print("I claim no credit for the idea of this game. ")
print("Please ennjoy my Python implementation of Wordle.")
while True:
    HANDLE = open('zwords.txt')
    words = HANDLE.read().split(', ')
    HANDLE.close()
    try:
        gotit = False
        word = randchoose(words)
        print()
        print()
        print("Word picked!")
        print()
        i = 0
        while i < 6:
            i = i +1
            inp = input("Enter word: ").upper()
            if inp == "LEMME IN!!":
                print("OK, OK, here it is: "+word)
            if inp not in words:
                print("Not a word.")
                i = i - 1
                continue
           
            print("The result is", evalinp(inp, word))
            print()
            if evalinp(inp, word) == "GGGGG":
                print("You got it! That took you", i, "tries!")
                gotit = True
                break
        if not gotit:
            print("Out of tries. :(")
            print("The word was", word)
    except:
        x = 2
