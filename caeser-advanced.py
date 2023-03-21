from math import floor
from copy import copy

def middle(num):
    if num >= 100:
        return int(str(num)[1:-1])
    else:
        return middleSquare(num * 10 + 110)

m = middle

def gen(seed):
    k = seed + 10
    return (k ** floor(k/2 + 1)) % 17576

threeLetterCompounds = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for L1 in alphabet:
    for L2 in alphabet:
        for L3 in alphabet:
            threeLetterCompounds.append(L1 + L2 + L3)
LCmodif = copy(threeLetterCompounds)

def createEncryptionDictionary(key):
    r = {}
    LCmodif = copy(threeLetterCompounds)
    ecomp = gen(key)
    for i in range(len(threeLetterCompounds)):
        try:
            comp = threeLetterCompounds[i]
            ecomp = gen(ecomp) % len(LCmodif)
            r[comp] = LCmodif[ecomp]
            del LCmodif[ecomp]
        except:
            print(ecomp)
            break
    return r

def createDecryptionDictionary(key):
    r = {}
    LCmodif = copy(threeLetterCompounds)
    ecomp = gen(key)
    for i in range(len(threeLetterCompounds)):
        try:
            comp = threeLetterCompounds[i]
            ecomp = gen(ecomp) % len(LCmodif)
            r[LCmodif[ecomp]] = comp
            del LCmodif[ecomp]
        except:
            print(ecomp)
            break
    return r


ced = createEncryptionDictionary
cdd = createDecryptionDictionary

def encmessage(message, key):
    enc = ""
    encDict = ced(key)
    for x in range(0, len(message), 3):
        enc = enc + encDict[message[x:x+3]]
    return enc

def decmessage(message, key):
    enc = ""
    encDict = cdd(key)
    for x in range(0, len(message), 3):
        enc = enc + encDict[message[x:x+3]]
    return enc

#print(encmessage("DIFFIEHELLMANKE", 2))
#print(decmessage(encmessage("DIFFIEHELLMANKE", 2), 2))




while True:
    key = int(input("Key?: "))
    message = input("Message?: ").upper()
    ed = input("Would you like to encrypt(default) or decrypt(D)?: ")

    CAESAR = {}
    A_CAESAR = {}
    for a in range(26):
        CAESAR[alphabet[a]] = alphabet[(a + key) % 26]
        A_CAESAR[alphabet[a]] = alphabet[(a - key) % 26]
    if ed == "D":
        enc = ""
        encDict = cdd(key)
        for x in range(0, len(message), 3):
            #print(x, x+3, message, message[x:x+3])
            snippet = message[x:x+3]
            try:
                enc = enc + encDict[snippet]
            except:
                encSnippetLetters = []
                for char in snippet:
                    if char.isalpha():
                        encSnippetLetters.append(A_CAESAR[char])
                    else:
                        encSnippetLetters.append(char)
                snippetLS = ''.join(encSnippetLetters)
                
                enc = enc + snippetLS
        #enc = enc + endBit
        print("The decrypted message is", enc)
        
    else:
        enc = ""
        encDict = ced(key)
        for x in range(0, len(message), 3):
            #print(x, x+3, message, message[x:x+3])
            snippet = message[x:x+3]
            try:
                enc = enc + encDict[snippet]
            except:
                encSnippetLetters = []
                for char in snippet:
                    if char.isalpha():
                        encSnippetLetters.append(CAESAR[char])
                    else:
                        encSnippetLetters.append(char)
                snippetLS = ''.join(encSnippetLetters)
                
                enc = enc + snippetLS
        #enc = enc + endBit
        print("The encrypted message is", enc)
    print()
              
        
    
    
        
