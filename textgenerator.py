import random

def makeTwoLists(d):
    l1 = list(d.keys())
    l2 = []
    for k in l1:
        l2.append(d[k])
    return [l1, l2]

f_21 = {}
f_11 = {}
f_1 = {}
handle = open("zsamptext.txt", "r")
sample_text = handle.read()
handle.close()
sample_text = sample_text.upper()
sample_text = sample_text.replace("\n", " ")
sample_text = sample_text + sample_text[:2]
f_21[sample_text[0] + sample_text[1]] = {}
f_11[sample_text[0]] = {}
for i in range(len(sample_text)):
    print(i)
    if i > 1:
        if sample_text[i-2] + sample_text[i-1] in f_21.keys():
            if sample_text[i] in f_21[sample_text[i-2] + sample_text[i-1]].keys():
                f_21[sample_text[i-2] + sample_text[i-1]][sample_text[i]] = f_21[sample_text[i-2] + sample_text[i-1]][sample_text[i]] + 1
            else:
                f_21[sample_text[i-2] + sample_text[i-1]][sample_text[i]] = 1
        else:
            f_21[sample_text[i-2] + sample_text[i-1]] = {sample_text[i]:1}
    
    if i > 0:
        if sample_text[i-1] in f_11.keys():
            if sample_text[i] in f_11[sample_text[i-1]].keys():
                f_11[sample_text[i-1]][sample_text[i]] = f_11[sample_text[i-1]][sample_text[i]] + 1
            else:
                f_11[sample_text[i-1]][sample_text[i]] = 1
        else:
            f_11[sample_text[i-1]] = {sample_text[i]:1}
    if sample_text[i] in f_1.keys():
        f_1[sample_text[i]] = f_1[sample_text[i]] + 1
    else:
        f_1[sample_text[i]] = 1
##    print(f_21)
##    print()
##    print(f_11)
##    print()
##    print(f_1)


text = ""
textLength = 10000
m2lf1 = makeTwoLists(f_1)
text = text + random.choices(m2lf1[0], weights=m2lf1[1])[0]

m2lf11 = makeTwoLists(f_11[text[0]])
text = text + random.choices(m2lf11[0], weights=m2lf11[1])[0]

print(text)
prev2 = text[0] + text[1]
for i in range(textLength):
    m2lf21 = makeTwoLists(f_21[prev2])
    addon = random.choices(m2lf21[0], weights=m2lf21[1])[0]
    text = text + addon
    prev2 = prev2[1] + addon
    print(addon, end="")

#print(text)




    
        
    
