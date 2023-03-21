from random import *

def rolldie(pdic):
    outcomes = []
    probs = []
    for i in pdic.keys():
        outcomes.append(i)
        probs.append(pdic[i])
    r = random()
    account = 0
    for ix in range(len(probs)):
        p = probs[ix]
        o = outcomes[ix]
        if r < account + p:
            return o
        account = account + p

##outcome = []
##tests = 1000000
##for i in range(tests):
##    outcome.append(rolldie({"A":0.5, "B":0.25, "C":0.25}))
##print(outcome.count("A")/tests)
##print(outcome.count("B")/tests)
##print(outcome.count("C")/tests)
def encode(edic, s):
    r = ''
    for c in s:
        r = r + edic[c]
    return r

def invertdict(dic):
    r = {}
    for k, v in zip(dic.keys(), dic.values()):
        r[v] = k
    return r
#print(invertdict({1:2, 3:4, 5:6}))
def isclear(edic, enc, dec):
    c = True
    highlighted = ''
    for cursor in range(len(enc)):
        if not c:
            return False
        ours = ''
        highlighted = highlighted + enc[cursor]
        if highlighted in edic.keys():
            ours = ours + edic[highlighted]
            c = ours == dec[:len(ours)]
            highlighted = ''
    return True
#print(encode({"I":"O", "O":"I"}, "IOIIO"))
def js(ls):
    r = ''
    for i in ls:
        r = r + i
    return r
#print(js(["a", "b", "c"]))
while True:
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = a[:int(input("How many letters?: "))]
    probs = {}
    for let in letters:
        probs[let] = float(input("What is the probability(1 - 0) of "+let+"?: "))
    print("Those probabilities sum to", sum(list(probs.values())))
    edic = {}
    for let in letters:
        edic[let] = input("Encoding for "+let+"?: ")
    outs = []
    for n in range(int(input("How many runs?: "))):
        newlet = rolldie(probs)
        outs.append(newlet)
    outs = js(outs)
    enc = encode(edic, outs)
    print("The text that was encrypted was", outs)
    print("The encrypted version is, ",  enc)
    print("The encrypted version is", len(enc), "letters long.")
    print("Your score is", len(enc)/len(outs))
    if isclear(invertdict(edic), enc, outs):
        print("It is also not ambiguous.")
    else:
        print("However, it is ambiguous.")
    print()
        
