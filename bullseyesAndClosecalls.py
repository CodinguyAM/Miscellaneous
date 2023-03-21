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

left = list(range(1000, 10000))
myNumber = choice(left)

while True:
    theirGuess = int(input("It's your turn. Which number do you guess?: "))
    result = compute(myNumber, theirGuess)
    if result == (4, 0):
        print("You won!")
        break
    print("That is", result[0], "bulls-eyes and", result[1], "cows.")
    print()
    myGuess = choice(left)
    print("I guess", myGuess)
    bulls = int(input("How many bulls-eyes?: "))
    cows = int(input("How many close calls?: "))
    
    if (bulls, cows) == (4, 0):
        print("I win!")
        print("You picked", myGuess)
        print("I picked", myNumber)
        break
    left = whittle(left, myGuess, bulls, cows)
    #print(left)
    print("I have", round((13.1 - log(len(left), 2)), 2), "bits of information. That is", round(((13.1 - log(len(left), 2))/0.131), 2), "percent")
    print()
