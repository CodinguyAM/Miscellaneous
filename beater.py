import random

handle = open("zstuff.txt", "r")
R = handle.read()
handle.close()
T = R.split(";")
WT = T[0].split()
LT = T[1].split()
for n in range(len(WT)):
    WT[n] = int(WT[n])
for n in range(len(LT)):
    LT[n] = int(LT[n])

#Grime dice
red = [2, 2, 2, 7, 7, 7]
blue = [1, 1, 6, 6, 6, 6]
green = [0, 5, 5, 5, 5, 5]
yellow = [4, 4, 4, 4, 4, 9]
magenta = [3, 3, 3, 3, 8, 8]

#faces
ZERO = '''
 -
'''
ONE = '''
 .
'''
TWO = '''.

  .'''
THREE = '''.
 .
  .'''
FOUR = '''. .

. .'''
FIVE = '''. .
 .
. .'''
SIX = '''...

...'''
SEVEN = '''...
 .
...'''
EIGHT = '''...
. .
...'''
NINE = '''...
...
...'''
NUMERALS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
#functions
def randchoose(ls):
    return ls[random.randint(0, len(ls)-1)]

def show(num):
    global NUMERALS
    n = NUMERALS
    print(n[num])

def roll(d):
    return randchoose(d)

def pick(o):
    if o == "r":
        return "magenta"
    if o == "b":
        return "red"
    if o == "g":
        return "blue"
    if o == "y":
        return "green"
    if o == "m":
        return "yellow"

print("Hello and welcome to Beater!")
print("This program uses a set of dice and carefully picks which one will beat yours when you input a dice.")
print()
print("These dice are not normal, 1-6 dice.")
print()
print("They are as follows:")
print()
print("Blue: 1-in-3 chance of 1, 2-in-3 chance of 6")
print("Green: 1-in-6 chance of 0, 5-in-6 chance of 5")
print("Magenta: 2-in-3 chance of 3, 1-in-3 chance of 8")
print("Red: 1-in-2 chance of 2, 1-in-2 chance of 7")
print("Yellow: 5-in 6 chance of 4, 1-in-6 chance of 9")
while True:
    WT[0] = WT[0] + 1
    LT[0] = LT[0] + 1
    print()
    d = input("Which dice would you like to roll?: ")
    print()
    his  = eval("roll(%s)" % d)
    print("Let's see what came up.")
    show(his)
    print("A", his)
    print()
    m = pick(d[0])
    mine = eval("roll(%s)" % m)
    print("I picked %s" % m)
    print()
    print("Let's see what came up.")
    show(mine)
    print("A", mine)
    print()
    if his > mine:
        print("I'll beat you next time!")
        LT[1] = LT[1] + 1
    if his == mine:
        print("Tied!")
    if his < mine:
        print("Told you so!")
        WT[1] = WT[1] + 1
    print("The current wins:total percentage is about", int((WT[1]/WT[0])*100))
    print("The current losses:total percentage is about", int((LT[1]/LT[0])*100))
    print("The Beater's score is currently", int((WT[1]/WT[0])*100)-int((LT[1]/LT[0])*100))
    w = open("zstuff.txt", "w")
    w.write(str(WT[0])+" "+str(WT[1])+";"+str(LT[0])+" "+str(LT[1]))
    w.close()
    q = input("Would you like to keep playing? (y/n): ")
    if q == "E1337":
        print("E1337")
    if q == "ASCII ART":
        print('''

$$$$$.$$$$$
$$$$.$.$$$$
$$$.$$$.$$$
$$.$$$$$.$$
$.........$
$.$$$$$$$.$
$.$$$$$$$.$
$.$$$$$$$.$

''')
    if q == "n":
        break
