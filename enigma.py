import math

rotorIShift = 0
rotorIIShift = 0
rotorIIIShift = 0

def middleSquare(num):
    if num >= 100:
        return int(str(num ** 2)[1:-1])
    else:
        return middleSquare(num + 100)
 
def gen(s):
    k = s + 10
    return (k ** math.floor(k/2)) % 26

def reverseDictionary(d):
    k = list(d.keys())
    v = list(d.values())
    r = {}
    for E in range(len(v)):
        r[v[E]] = k[E]
    return r

def createRotor(starts, ends):
    s = list(starts)
    e = list(ends)
    r = {}
    for k in range(len(s)):
        r[s[k]] = e[k]
    return r

rotorI = createRotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "QWERTYUIOPASDFGHJKLZXCVBNM")
rotorII = createRotor("QWERTYUIOPASDFGHJKLZXCVBNM", "MNBVCXZLKJHGFDSAPOIUYTREWQ")
rotorIII = createRotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "QWERTYUIOPASDFGHJKLZXCVBNM")

def posInAlphabet(a):
    for k in range(26):
        if "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[k] == a:
            return k

def encode(l, r, s=0):
    if l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
       return r["ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(posInAlphabet(l) + s) % 26]]
    else:
        return l
def decode(l, r, s):
    if l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(posInAlphabet(encode(l, reverseDictionary(r))) - s) % 26]
    else:
        return l


print("The Enigma Machine!")
print("Hi User! If you're encrypting a message, first set a key. Make sure to pass the key AND the message! And remember - the key must be a positive number. ")
print("For a person decrypting an Enigma message, you'll need a key. If you don't have a key, good luck. The chances of getting it right randomly are 1 in 17,576.")
print()
while True:
    seed = int(input("What is your key?: "))
    rotorIShift = gen(seed)
    rotorIIShift = gen(middleSquare(seed))
    rotorIIIShift = gen(middleSquare(middleSquare(seed)))

    m = input("What message will you be encrypting or decrypting?: ")
    m = m.upper()
    
    ed = input("Would you like to encrypt(E) or decrypt(D)?: ")
    if ed == "D":
        dm = ""
        count = len(m)
        rotorIShift = rotorIShift + count
        rotorIIShift = rotorIIShift + math.floor(count/2)
        rotorIIIShift = rotorIIIShift + math.floor(count/3)
        for c in m[::-1]:
            
##            print("Count", count)
##            print("Processing letter", c)
##            print(rotorIShift, rotorIIShift, rotorIIIShift)
            m3 = decode(c, rotorIII, rotorIIIShift)
            #print(m3, "Before R3")
            m2 = decode(m3, rotorII, rotorIIShift)
            #print(m2, "Before R2")
            m1 = decode(m2, rotorI, rotorIShift)
            #print(m1, "Before R1")
            rotorIShift = rotorIShift - 1
            if count % 2 == 0:
                #print("rotating R2")
                rotorIIShift = rotorIIShift - 1
            if count % 3 == 0:
                #print("rotatibng R3")
                rotorIIIShift = rotorIIIShift - 1
            
            
            dm = dm + m1
            count = count - 1
        dm = dm[::-1]
        print("The decrypted version is", dm)
    else:
        em = ""
        count = 0
        for c in m:
            count = count + 1
            #print("Count", count)
            #print("Processing", c)
            if count % 2 == 0:
                #print("rotating R2")
                rotorIIShift = rotorIIShift + 1
            if count % 3 == 0:
                #print("rotating R3")
                rotorIIIShift = rotorIIIShift + 1
            rotorIShift = rotorIShift + 1
            #print(rotorIShift, rotorIIShift, rotorIIIShift)
            m1 = encode(c, rotorI, rotorIShift)
            #rint(m1, "At R1")
            m2 = encode(m1, rotorII, rotorIIShift)
            #print(m2, "At R2")
            m3 = encode(m2, rotorIII, rotorIIIShift)
            #print(m3, "At R3")
            em = em + m3
        print("The encrypted version is", em)
    print()
