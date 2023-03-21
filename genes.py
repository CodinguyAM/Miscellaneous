import random

def randchoose(ls):
    return ls[random.randint(0, len(ls)-1)]

def p(CHROMOSOMES=8, MIN=10, MAX=20):
    MULTS = ["0.5x", "1.0x", "1.5x", "2.0x"]
    #build NUMS
    NUMS = []
    for x in range(MAX):
        if x >= MIN:
            NUMS.append(str(x+1))
    VALS = [MULTS, NUMS]
    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:CHROMOSOMES]
    person = ""
    for n in ALPH:
        person = person + n + randchoose(randchoose(VALS)) + " "
    return person



def baby(p1, p2, hushed=False):
    b = ""
    if not hushed:
        print("Parent 1:", p1)
        print("Parent 2:", p2)
        print()
    p1g = p1.split()
    p2g = p2.split()
    for c in range(len(p1g)):
        p1c = p1g[c]
        p2c = p2g[c]
        
        try:
            p1v = int(float(p1c[1:]))
        except:
            p1v_m = float(p1c[1:len(p1c)-1])
        try:
            p2v = int(float(p2c[1:]))
        except:
            p2v_m = float(p2c[1:len(p2c)-1])
        #print(p1c, p2c)
        if p1c[len(p1c)-1] == "x":
            if p2c[len(p2c)-1] == "x":
                add = p1c[0] + str((p1v_m + p2v_m)/2) + "x "
            else:
                add = p1c[0] + str(p1v_m * p2v) + " "
        else:
            if p2c[len(p2c)-1] == "x":
                add = p1c[0] + str(p1v * p2v_m) + " "
            else:
                if p1v > p2v:
                    add = p1c[0]+ str(p1v) + " "
                if p1v <= p2v:
                    add = p1c[0]+ str(p2v) + " "
        b = b + add
    if not hushed:
        print("Baby:", b)
    return b

def marry(people, gen_num, hushed=False):
    if not hushed:
        print()
        print("Generation", gen_num)
    #print(people)
    babies = []
    for n in range(int(len(people)/2)):
        if not hushed:
            print()
            chutku = baby(people[2*n], people[(2*n)+1])
        else:
            chutku = baby(people[2*n], people[(2*n)+1], True)
        babies.append(chutku)
    if not hushed:
        print()
    return babies

def genpeople(num, CHRS=8, MIN=10, MAX=20):
    r = []
    for oof in range(num):
        r.append(p(CHRS, MIN, MAX))
    return r

print("This is Advay's Gene Program!")
while True:
    chrs = int(input("Chromosomes?(25 at most): "))
    mini = int(input("Minimum value for a (numerical) chromosome at beginning?: "))
    maxi = int(input("Maximum value for a (numerical) chromosome at beginning?: "))
    if input("Enter Q to quit: ") == "Q":
        break
    print()
    parent1 = p(chrs, mini, maxi)
    parent2 = p(chrs, mini, maxi)
    b1 = baby(parent1, parent2)
    print()
    print("Now that you know how it works, let's get going!")
    print()
    gens = int(input("No. of Generations?: "))
    hushed = not bool(input("Would you like to print the parents and babies and so on, or just get the 'natural selection-approved' final result?(K, then enter for yes, and just enter for no)"))
    print()
    print()
    people = genpeople(2**gens, chrs, mini, maxi)
    genNum = gens
    while len(people) > 1:
        people = marry(people, genNum, hushed)
        genNum = genNum - 1
    print()
    print("Final:", people[0])
    print()
    print("Those", gens, "generations took not very long!")
    print()
    print()
    print()
    print()
print("Thank you for using my gene program!")
