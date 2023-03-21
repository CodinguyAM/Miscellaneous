try:

    from random import *
    import math

    goal = 1500
    low = -1.5
    high = 1.5
    
    #companies = ["d'Oulah And Sons", "Yumy Foods Inc.", "Kriate", "Kandoku Quality Electronics", "Bankraft"]
    companies = ["1", "2", "3", "4", "5"]
    stockValues = {companies[0]:10.00, companies[1]:11.25, companies[2]:200.00, companies[3]:15.55, companies[4]:1.00}
    stockIndex = 0
    myMoney = 200
    myShares = {companies[0]:0, companies[1]:0, companies[2]:0, companies[3]:0, companies[4]:0}
    mySharesValue = 0
    isAverage = True

    def nearestHundreth(n):
        return 0.01*(math.floor(n*100))
    def faireningAverage(s):
        total = (len(s)+1)/len(s)
        for i in s:
            total = total * i
        return 100*nearestHundreth(total**(1/len(s))) - 332
    def evolve(stockPrice):
        growth = random() - uniform(low, high)
        growthPerShare = growth * stockPrice
        if nearestHundreth(stockPrice + growthPerShare) > 0.01:
            return nearestHundreth(stockPrice + growthPerShare)
        else:
            return 0.01

    def sharesRem(stockPrice):
        def f(p):
            return p**2 - 19*p + 40
        def F(x):
            return abs(f(1/x) - f(x) + f(2*x))
        r = F(stockPrice/20)
        r = math.floor(r)
        if r > 100:
            r = 100
        if r < 10:
            r = r + 10
        return r

    def evolveMarket(market):
        m = market
        for k in market.keys():
            m[k] = evolve(market[k])
        return m

    
    print("This is a stock exchange program")
    print("Here's how to play!")
    print()
    print("There are", len(companies) ," companies in this market.")
    print("Their names are: ")
    for c in companies:
        print(c)
    print("You can buy and sell shares each turn. The price of each stock changes, so be careful!")
    print()
    while isAverage:
         print("Here's the situation in the stock market")
         oldStockIndex = stockIndex
         stockIndex = int(faireningAverage(stockValues.values()))
         if oldStockIndex > stockIndex:
            diff = str(int(oldStockIndex - stockIndex))+" down"
         else:
            diff = str(int(stockIndex - oldStockIndex))+" up"
         print("The current stock index in this exchange is", stockIndex, ". That's", diff)
         for c in companies:
             print(c, ":", stockValues[c], "dollars per share")
         print()
         print("Here's your shares situation")
         for k in myShares.keys():
             print(myShares[k], "shares of", k)
             mySharesValue = mySharesValue + myShares[k] * stockValues[k]
         print("You have", myMoney, "dollars")
         print("You also have", mySharesValue, "dollars' worth of shares.")
         print()
         print("Speaking of which, people have bought: ")
         for c in companies:
             print(100 - sharesRem(stockValues[c]), "shares of", c)
         print()
         companiesBought = int(input("How many of the companies would you like to buy shares from?: "))
         print("OK")
         print()
         for i in range(companiesBought):
             comp = input("Which company would you like to buy shares from?: ")
             am = int(input("How many shares would you like to buy of "+comp+"?: "))
             remainingShares = sharesRem(stockValues[comp]) - myShares[comp]
             if am > remainingShares:
                 print("Sorry, that is more than the number of shares available. Buying", remainingShares, "shares instead.")
                 am = remainingShares
             myMoney = myMoney - stockValues[comp] * am
             myShares[comp] = myShares[comp] + am
         
         companiesSold = int(input("How many of the companies would you like to sell shares from?: "))
         print("OK")
         print()
         for i in range(companiesSold):
             comp = input("Which company would you like to sell shares from?: ")
             am = int(input("How many shares would you like to sell of "+comp+"?: "))
             if am > myShares[comp]:
                 print("Sorry, that is more than the number of shares available. Selling", myShares[comp], "shares instead.")
                 am = myShares[comp]
             myMoney = myMoney + stockValues[comp] * am
             myShares[comp] = myShares[comp] - am
         if myMoney < 0:
             print("You are broke. :( Play another time, hopefully you'll have better luck!")
             isAverage = False
         if myMoney > goal:
             print("You won with",  str(myMoney)+" dollars!")
             print("That's", myMoney - goal, "dollars more than the goal of", goal)
             isAverage = False
         stockValues = evolveMarket(stockValues)
         mySharesValue = 0
except:
    print("We encountered an error. If you are the person who made this program, please fix it.")

