from random import randint
A = 0
B = 0
def turn(Q, S):
    #print("Q is", Q)
    #print("S is", S)
    hr = input("Hold(H) or Roll(R)?: ")
    if hr == "R":
        R = randint(1, 6)
        if R == 1:
            print("Oopsy. Pig Out.")
            return S + 1
        print("That's a", R)
        return turn(Q+R, S)
    elif hr == "H":
        print("Holding...")
        print("Held!")
        return S + Q
    else:
        return S
goal = int(input("What's the Bar?: "))
Aname = input("Player A Name: ")
Bname = input("Player B Name: ")
#print("Value o' goal = ", goal)
HB = "Mumma@1st"
if input("Super Passy Wordy Password!: ") == HB:
    while True:
        print("It's %s's turn now" % Aname)
        A = turn(0, A)
        #print("Value o' a ", A)
        print("Hey" , Aname, "! You're at a good", A)
        print("It's %s's turn now" % Bname)
        B = turn(0, B)
        print("Hey" , Bname, "! You're at a good", B)
        if A >= goal:
            print("Yay yay yay yay yay yay! You won, %s!" % Aname)
            print("For the record, %s won" % Aname)
            break
        if B >= goal:
            print("Yay yay yay yay yay yay! You won, %s!" % Bname)
            print("For the record, %s won" % Bname)
            break
    
    
