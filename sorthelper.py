def indice(l, x, flip=False):
    m = 1
    l.sort(reverse=(not flip))
    #print(l)
    if flip:
        m = -1
    for n in range(len(l)):
        y = l[n]
        if y * m < x * m:
            return n
    return len(l)

while True:
    data = input('Numbers: ').split('	')[1:]
    skipped = 0
    for n in range(len(data)):
        try:
            try:
                data[n - skipped] = int(data[n])
            except:
                data[n - skipped] = float(data[n])
        except:
            del data[n - skipped]
            skipped = skipped + 1
            
    n = input('Placing: ')
    try:
        n = int(n)
    except:
        n = float(n)
    flip = bool(input('Is this criterion bad? Type anything for yes, dont for no: '))
    print()
    i = indice(data, n, flip)
    print(str(i + 1) + "th", "out of", len(data) + 1)
    print("Putting it at the", str(100 - int(10000*( (i)/len(data))) /100) + "th", "percentile")
    print("Putting it at the", str(100 - int(10000*( (i+1)/(len(data)+1))) /100) + "th", "percentile")
    print()
    print()
