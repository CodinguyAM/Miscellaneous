import random

sp_chars = "!@#$%^&*"
sp_chars2 = "/\,.:;"
nums = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
banks = [sp_chars, sp_chars2, nums, letters, capital]

def show(ls):
    for n in list(range(len(ls))):
        #print(type(n))
        print(str(n+1)+". ", ls[n])

def choose(ls):
    return ls[random.randint(0, len(ls) - 1)]

def insert(to, what, loc):
    #print(to, what, loc)
    bef = to[:loc]
    aft = to[loc:]
    return bef + what + aft

def gen_next():
    global banks
    cat  = choose(banks)
    return choose(cat)

def gen_n_pass(leng):
    pas = ""
    for n in [["n"] * leng][0]:
        pas = pas + gen_next()
    return pas
        
def gen_pass(leng, reqs):
    if reqs == []:
        return gen_n_pass(leng)
    else:
         req = choose(reqs)
         normpass = gen_n_pass(leng)
         ii = random.randint(0, leng - 1)
         return insert(normpass, req, ii)

print("Welcome to SecurPass- where you can find secure passwords!")
print("Press K at the candidates prompt to exit")
while True:
    cands = input("How many password candidates would you like to generate? Only one will be printed as your password: ")
    if cands == "k":
        break
    else:
        cands = int(cands)
    reqs = input("Anything your password should have? Put it in here(separate different things by spaces, if you do only one will be put in): ").split()
    leng = int(input("Password length?: "))
        
    passes = []
    for n in [["n"] * cands][0]:
        passes.append(gen_pass(leng, reqs))

    print("Your password is:", choose(passes))
    b = input("To view all candidates, enter -b: ")
    if b == "-b":
        print()
        show(passes)
    print()
print()
print("Thank you for using SecurPass - where you can find secure passwords!")
