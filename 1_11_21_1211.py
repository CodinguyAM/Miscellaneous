def allsame(x):
    rv = True
    for y in list(range(0, len(x))):
        if x[y] != x[y-1]:
            rv = False
    return rv
def rem(ls):
    #print("REM initialized")
    #print(ls, "INPUT")
    if ls == "":
        return "spop"
    if allsame(ls):
        rmf = ls
        rtf = ""
    else:
        rmf = ls[0]
        if len(ls) > 1:
            rtf = ls[1:]
        else:
            rtf = ""
    for x in list(range(0, len(ls))):
        if ls[x] != ls[x-1] and x != 0:
            #print(x, "X")
            rmf = ls[:x]
            rtf = ls[x:]
            break
    #print(rmf, rtf, "RMFRTFb")
    return (rmf, rtf)
def nnum(ls):
    num = ""
    if ls == "":
        return "No input, no good output!"
    while  True:
        #print(ls, "LS")
        if rem(ls) == "spop":
            #print("Spopped out")
            break
        else:
            #print("RMFRTF intialized")
            rmf, rtf = rem(ls)
            #print(rmf, rtf, "RMFRTF")
            num = num + str(len(rmf)) + rmf[0]
            #print(num, "NUM")
            ls = rtf
    return num


o = input("Hello and Welcome to 1 11 21 1211 111221...! Enter your seed: ")
while True:
    p = nnum(o)
    print(p)
    print()
    o = p
        
                
            
