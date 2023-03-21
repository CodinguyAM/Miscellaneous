import random

A = "A"
B = "B"
C = "C"
propVals = {"E. 51st Street":400, "Fifth Avenue":350, "Downtown":450, "Broadway":500, "United Nations Plaza":750, "Rockefeller Building":775, "Freedom Tower":800, "Chrysler Building":700, "Statue of Liberty":1500}
PropGrps = {"E. 51st Street":A, "Fifth Avenue":B, "Downtown":A, "Broadway":C, "United Nations Plaza":B, "Rockefeller Building":C, "Freedom Tower":A, "Chrysler Building":B, "Statue of Liberty":C}
props = ["E. 51st Street", "Fifth Avenue", "Downtown", "Broadway", "United Nations Plaza", "Rockefeller Building", "Freedom Tower", "Chrysler Building", "Statue of Liberty"]
def droll():
    return random.randint(-2, 2)
def wherenext(where):
    if where == "GO":
        return 0
    elif where == "CHANCE":
        return 4
    elif where == 8:
        return "GO"
    elif where == 3:
        return "CHANCE" 
    else:
        return where+1
def hasgroups(props):
    global PropGrps
    grp = []
    ret = []
    for st in props:
        grp.append(PropGrps[st])
    for q in ["A", "B", "C"]:
        if grp.count(q) == 3:
            ret.append(q)
    return ret
def t(P, A, Q):
    return [P+Q, A-Q]
wa = 0
wb = 0
wc = 0
am = 945
bm = 945
cm = 945
ap = []
bp = []
cp = []
ah = []
bh = []
ch = []
while True:
    try:
        at = props[wa]
    except:
        at = wa
    print("A, you are at", at)
    if (not at in bp) and (not at in cp) and (not at in ap) and (type(at) != 'str'):
        yn = input("Will you buy "+ at+ "? It's "+ str(propVals[at])+ " dollars! Press Y or N: ")
        if yn == "y":
            am = am - propVals[at]
            ap.append(at)
    elif at in ap:
        print("Blastoof!")
        am = am + 50
    elif at in bp:
        l = t(bm, am, propVals[at]*2)
        bm = l[0]
        am = l[1]
    elif at in cp:
        l = t(cm, am, propVals[at]*2)
        cm = l[0]
        am = l[1]
    elif at == "GO":
        am = am + 75
    elif at == "CHOICE":
        am = am + droll()*50
    wa= wherenext(wa)




        
    try:
        at = props[wb]
    except:
        at = wb
    print("B, you are at", at)
    if (not at in bp) and (not at in cp) and (not at in ap) and (type(at) != 'str'):
        yn = input("Will you buy "+ at+ "? It's "+ str(propVals[at])+ " dollars! Press Y or N: ")
        if yn == "y":
            bm = bm - propVals[at]
            bp.append(at)
    elif at in bp:
        print("Blastoof!")
        bm = bm + 50
    elif at in ap:
        l = t(am, bm, propVals[at]*2)
        am = l[0]
        bm = l[1]
    elif at in cp:
        l = t(cm, bm, propVals[at]*2)
        cm = l[0]
        bm = l[1]
    elif at == "GO":
        bm = bm + 75
    elif at == "CHOICE":
        bm = bm + droll()*50
    wb = wherenext(wb)





    
    try:
        at = props[wc]
    except:
        at = wc
    print("C, you are at", at)
    if (not at in bp) and (not at in cp) and (not at in ap) and (type(at) != 'str'):
        yn = input("Will you buy "+ at+ "? It's "+ str(propVals[at])+ " dollars! Press Y or N: ")
        if yn == "y":
            cm = cm - propVals[at]
            cp.append(at)
    elif at in cp:
        print("Blastoof!")
        cm = cm + 50
    elif at in bp:
        l = t(bm, cm, propVals[at]*1.2)
        bm = l[0]
        cm = l[1]
    elif at in ap:
        l = t(am, cm, propVals[at]*1.2)
        am = l[0]
        cm = l[1]
    elif at == "GO":
        cm = cm + 75
    elif at == "CHOICE":
        cm = cm + droll()*50
    wa= wherenext(wa)




        



    
        
        
        
        
    


