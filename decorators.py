cachelist = [{}]
def dn():
    pass
namesdict = {dn:0}

def _2l(d):
    r = tuple(d.keys())
    return (r, tuple([d[k] for k in r]))

def memo(func):
    global cachelist, namesdict
    if func in namesdict:
        name = namesdict[func]
    else:
        namesdict[func] = max(namesdict.values()) + 1
        name = namesdict[func]
    if len(cachelist) == name:
        cachelist.append({})
    cache = cachelist[name]
    def rf(*args, **kwargs):
        if tuple([args, _2l(kwargs)]) in cache.keys():
            #print('MEMO DEBUG: In Cache!!')
            return cache[tuple([args, _2l(kwargs)])]
        r = func(*args, **kwargs)
        cache[tuple([args, _2l(kwargs)])] = r
        return r
    return rf

@memo
def add(x, y):
    return x + y

print(add(2, 3))
print(add(2, 3))
print(add(3, 4))
print(add(3, 4))
print(add(2, 3))
