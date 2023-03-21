import random
print("Welcome to Four Weighings")
print("There are 9 identical keys. 8 of them are fake and 1 is real. The real key will open the prison door and you will be free!  But the fake ones will explode a bomb. Additionaly, there is a secret hallway to freedom after the door where you will say wether the kye is lihgter orheavier than the rest...")
def weigh(left, right):
    if left > right:
        return "LEFT"
    elif left < right:
        return "RIGHT"
    elif left == right:
        return "EQUAL"
keys = [1]*9
i = random.randint(0, 8)
c = random.randint(0, 1)
if c == 1:
    keys[i] = 1.1
elif c == 0:
    keys[i] = 0.9
#print(keys)
def aw():
    r = 0
    l = 0
    for h in input("Left Side: "):
        l = l + keys[int(h)-1]
    for q in input("Right Side: "):
        r = r + keys[int(q)-1]
    #print(l, r)
    print(weigh(l,r))
aw()
aw()
aw()
aw()
k = int(input("Key Numer: "))
k = k -1
if k == i:
    loh = input("L(0) or H(1): ")
    if int(loh)  == c:
        print("Freedom!")
    else:
        print("Sorry.")
else:
    print("Sorry. It was", str(i+1), "and", c)
