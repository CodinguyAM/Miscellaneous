import random as r 

def upd(cs, outcome):
    if len(cs) == 1:
        return str(outcome)
    else:
        return cs[:len(cs)-1] + str(outcome)

def outcomeOfFlip(p0):
    rn = r.random()
    if rn < p0:
        return "0"
    else:
        return "1"

def translateToRG(s):
    t = ""
    for i in s:
        if i == "0":
            t = t + "R"
        else:
            t = t + "G"
    return t

def translateTo01(s):
    t = ""
    for i in s:
        if i == "R":
            t = t + "0"
        else:
            t = t + "1"
    return t

##print(translateToRG("0100"))
##print(translateTo01("RRRG"))
##print(translateToRG(translateTo01("RGRG")))

def possibleSequences(n):
    ps = []
    for i in range(2**n):
        binn = bin(i)[2:]
        binn = "0"* (n-len(binn)) + binn
        ps.append(binn)
    return ps

##print(possibleSequences(3))
    
def DNO(outcome, outcomes_dic):
    return outcomeOfFlip(outcomes_dic[outcome])



def markovChain(its = None, hushed = False):
    prevOutcomes = ""
    allOut = ""
    try:
        memory = int(input("How much memory does this Markov machine have?: "))
    except:
        memory = 1
    for i in range(memory):
        prevOutcomes = prevOutcomes + outcomeOfFlip(0.5)
    allOut = prevOutcomes
    OD = {}
    for P in possibleSequences(memory):
        OD[P] = float(input("What is the probability of picking from R after "+translateToRG(P)+"?: "))
    if its == None:
        while True:
            nextFlip = DNO(prevOutcomes, OD)
            prevOutcomes = upd(prevOutcomes, nextFlip)
            allOut = allOut + nextFlip
            percentage = 100*(allOut.count("0")/len(allOut))
            if not hushed:
                print("Currently,", percentage, "% came up red")
                print("Also,", 100-percentage, "% came up green")
    else:
        its = its - memory
        for ransdomname in range(its):
            nextFlip = DNO(prevOutcomes, OD)
            prevOutcomes = upd(prevOutcomes, nextFlip)
            allOut = allOut + nextFlip
            #print(allOut.count("0"), len(allOut))
            percentage = 100*(allOut.count("0")/len(allOut))
            if not hushed:
                print("This one was a", translateToRG(nextFlip))
                print("Currently,", percentage, "% came up red")
                print("Also,", 100-percentage, "% came up green")
        print()
        print("", percentage, "% came up red")
        print("Also,", 100-percentage, "% came up green")
        print("The total list of outcomes is", translateToRG(allOut))
while True:
    try:
        p = input("#Iterations? Enter K to recieve a live flow(can be stopped by pressing CNTRL-C): ")
        if p == "K":
            p = None
            WATCH = True
        else:
            WATCH = False
            p = int(p)
        print()
        markovChain(its=p, hushed=not WATCH)
    except:
        print()
