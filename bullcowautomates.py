from random import choice
from math import log
def compute(number, guess):
    bulls = 0
    cows = 0
    number =  str(number)
    guess = str(guess)
    for position in range(len(guess)):
        digit = number[position]
        g_digit = guess[position]
        if g_digit == digit:
            bulls = bulls + 1
        elif number.count(g_digit) > 0:
            cows = cows + 1
    return (bulls, cows)

def whittle(left, guess, bulls, cows):
    whit = []
    for num in left:
        if compute(num, guess) == (bulls, cows):
            whit.append(num)
    return whit

games = 1
while True:
    print("START OF GAME", games)
    left = list(range(1000, 10000))
    left2 = list(range(1000, 10000))
    myNumber = choice(left)
    theirNumber = choice(left2)
    while True:
        theirGuess = choice(left2)
        print("A guesses", theirGuess)
        result = compute(myNumber, theirGuess)
        bulls = result[0]
        cows = result[1]
        if (bulls, cows) == (4, 0):
            print("A wins!")
            print("B picked", theirNumber)
            print("A picked", myNumber)
            break
        print("That is", bulls, "bulls-eyes and", cows, "close calls.")
        left2 = whittle(left2, theirGuess, bulls, cows)
        #print(left2)
        print("A has", round((13.1 - log(len(left2), 2)), 2), "bits of information. That is", round(((13.1 - log(len(left2), 2))/0.131), 2), "percent")
        print()
        
        myGuess = choice(left)
        print("A guesses", myGuess)
        result = compute(theirNumber, myGuess)
        bulls = result[0]
        cows = result[1]
        if (bulls, cows) == (4, 0):
            print("A wins!")
            print("B picked", theirNumber)
            print("A picked", myNumber)
            break
        print("That is", bulls, "bulls-eyes and", cows, "close calls.")
        left = whittle(left, myGuess, bulls, cows)
        #print(left)
        print("A has", round((13.1 - log(len(left), 2)), 2), "bits of information. That is", round(((13.1 - log(len(left), 2))/0.131), 2), "percent")
        print()
    print("END OF GAME", games)
    print("\n\n\n\n")
    games = games + 1
