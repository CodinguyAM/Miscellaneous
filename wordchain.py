print("Welcome to Word Chain or the Word End Game")
words = open("words.txt", "r").read()
words = words.split("\n")
nameI = input("Player I Name: ")
nameII = input("Player II Name: ")
nameIII = input("Player III Name: ")
def valid(w1, w2):
    return w1[-1] == w2[0] and w2 in words and w1 != w2
cword = input("Enter Word, %s: " % nameI)
while True:
    pword = cword
    while True:
        cword = input("Enter Word, %s: " % nameII)
        if valid(pword, cword):
            break
        else:
            print("oopsy")
    pword = cword
    while True:
        cword = input("Enter Word, %s: " % nameIII)
        if valid(pword, cword):
            break
        else:
            print("oopsy")
    pword = cword
    while True:
        cword = input("Enter Word, %s: " % nameI)
        if valid(pword, cword):
            break
        else:
            print("oopsy")
    
    
    
    
