def calc(linked, current):
    new = [0] * len(current)
    for x in range(len(current)):
        if linked[x] == []:
            new[x] = current[x]
    for x in range(len(current)):
        for lpage in linked[x]:
            new[lpage] = new[lpage] + current[x]/len(linked[x])
    return new

def issame(col1, col2):
    yes = True
    for x in range(len(col1)):
        if abs(col1[x]-col2[x]) > 10 ** -9:
            yes = False
    return yes

pages = int(input("Pages?: "))
print()
linked = [[]] * pages
current = [1/pages] * pages


for x in range(pages):
    lx = input("Pages page " + str(x) + " is linked to?: ").split(",")
    nlx = []
    for lxe in lx:
        if lxe != "":
            nlx.append(int(lxe))
    linked[x] = nlx

print()
while True:
    ncurrent = calc(linked, current)
    #print(current, sum(current))
    if issame(ncurrent, current):
        break
    current = ncurrent

for x in range(len(current)):
    print("Page", x, "has pageRank", round(current[x], ndigits=3))
    
