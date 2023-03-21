import random

def intput(s):
    r = input(s)
    try:
        r = int(r)
        return r
    except ValueError:
        r = float(r)
        return r
    except ValueError:
        return 0
    

class Bank:
    def __init__(self, name):
        self.accounts = [10]
        self.money = 10.0
        self.loans = []
        self.interest = 10
        self.name = name
    
    def loan(self, amount, v):
        self.loans.append([amount, self.interest, v])
        self.money = self.money - amount

    def isBankrupt(self):
        #print(self.money)
        return self.money <= 0

    def deposit(self, accid, m):
        if accid < len(self.accounts):
            if self.accounts[accid] > -1*m:
                self.accounts[accid] = self.accounts[accid] + m
                self.money = self.money + m

    def withdraw(self, accid, m):
        self.deposit(accid, -1 * m)

    def pay(self, loanid):
        if loanid < len(self.loans):
            self.money = self.money + self.loans[loanid][0]
            self.loans[loanid] = [0, 0, 0]

    def ma(self):
        self.accounts.append(10)
        self.money = self.money + 10

    def evolve(self, EI):
        print(self.name)
        #print(self.money)
        if not self.isBankrupt():
            print('You have $%i in the bank.' % int(self.money))
            print('The Economic Index is', EI)
            #print(self.accounts)
            print('Your investors have $%i collectively.' % int(sum(self.accounts)))
            print('')
            newI = intput('Interest Rate: ')
            self.interest = newI
            lostfl = 0
            for l in range(random.randint(0, 10)):
                rnd = random.random()
                lo = [int(self.money * 0.5 * rnd), 1-rnd]
                accept = intput('A request for a loan of %i, with a trustability of %f. Do you accept?: ' % (int(lo[0]), lo[1]))
                if accept:
                    self.loan(lo[0], lo[1])
                    lostfl = lostfl + lo[0]
            print('You have lost $%i from loaning. ' % int(lostfl))
            gainedfl = 0
            for e in range(len(self.loans)):
                self.loans[e][0] = self.loans[e][0] * (self.loans[e][1]/100)
                #print('recahed
                if random.random() < self.loans[e][2]:
                    gainedfl = gainedfl + self.loans[e][0]
                    self.pay(e)
            print('You have gained $%i from loans being paid back. ' % int(gainedfl))
            gainedfd = 0
            for ir in range(int(EI * len(self.accounts))):
                daindx = random.randint(0, len(self.accounts)-1)
                n = random.randint(0, int(self.accounts[daindx]))
                gainedfd  = gainedfd + n
                self.deposit(daindx, n)
            lostfd = 0
            for ir in range(int((1-EI) * len(self.accounts))):
                daindx = random.randint(0, len(self.accounts)-1)
                n = random.randint(0, int(self.accounts[daindx]))
                lostfd  = lostfd + n
                self.withdraw(daindx, n)
            print('You have lost $%i from withdrawals. ' % int(lostfd))
            print('You have gained $%i from deposits. ' % int(gainedfd))
            gainedfa = 0
            for ir in range(random.randint(1, int(EI * 5))):
                self.ma()
                gainedfa = gainedfa + 10
            print('You have gained $%i from new accounts. ' % int(gainedfa))
            for ds in range(len(self.accounts)):
                self.accounts[ds] = self.accounts[ds] * (1 + (self.interest/100))
            if not self.isBankrupt():
                print('You now have $%i. ' % int(self.money))
            else:
                print('You are now bankrupt, and $%i in debt.' % -1*int(self.money))
        else:
            print('You are now bankrupt, and $%i in debt.' % -1*int(self.money))
        print()
        print()
        print()

n = 1
banks = [Bank(input('Name?: ')) for x in range(n)]
EI = 0.5
while True:
    for b in banks:
        b.evolve(EI)
        EI = EI + (random.random()-0.5)/10
    
