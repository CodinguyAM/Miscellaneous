import random

def randchoose(ls):
    return ls[random.randint(0, len(ls)-1)]

def remove_from_string(string, r):
    ls = list(string)
    ls.remove(r)
    re = ""
    for e in ls:
        re = re + e
    return re
tiles = "AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYZ__"
#print(len(tiles))

while True:
    hand = input("Current Hand: ")
    for n in range(7-len(hand)):
        drawn = randchoose(tiles)
        tiles = remove_from_string(tiles, drawn)
        hand = hand + drawn
    print("Your refurbished hand is:", hand)
