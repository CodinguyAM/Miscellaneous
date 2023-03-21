import random
A = 0
B = 0
print("Halloo! You are a farmer. You want to get as many chickens as possible, but a fox both ends your turn and removes all the chickens.")
level = input("Do you want to play Easy(E), Regular(R) or Hard(H) Foxes and Hens?")
goal = int(input("Very Well Then. How many chickens will you gather? 1-100, please."))
Aname = input("Player A Name: ")
Bname = input("Player B Name: ")
if level == "H":
    deck = ["F", "F", "H"] * 400
elif level == "E":
    deck = ["F", "H", "H"] * 200
else:
    deck = ["F", "H"] * 400
def pickCard(deck):
    i = random.randint(0, len(deck)-1)
    saveIt = deck[i]
    del deck[i]
    return (saveIt, deck)
def turn(chickens, score, deck):
    gw = input("Will you gather(G) or wait(W)")
    if gw == "W":
        v = pickCard(deck)
        card = v[0]
        ndeck = v[1]
        if card == "F":
            print("Wait a moment... Where'd all your little chickies go?")
            return (score, ndeck)
        print("Another chiken!")
        print("There are now", chickens+1, "chikens in you barn/farm.")
        return turn(chickens+1, score, ndeck)
    elif gw == "G":
        print("Gathering..")
        print("Gathered!")
        return (score + chickens, deck)
    else:
        return (score, deck)
while True:
    print("It's %s's turn now" % Aname)
    w = turn(0, A, deck)
    deck = w[1]
    A = w[0]
    print(Aname ,"now has", A, "chickens")

    print("It's %s's turn now" % Bname)
    x = turn(0, B, deck)
    deck = x[1]
    B = x[0]
    print(Bname, "now has", B, "chickens")
    if A >= goal:
        print("Yay yay yay yay yay yay! You won, %s!" % Aname)
        print("For the record, %s won" % Aname)
        break
    if B >= goal:
        print("Yay yay yay yay yay yay! You won, %s!" % Bname)
        print("For the record, %s won" % Bname)
        break
