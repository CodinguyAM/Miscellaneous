whand = open('scrabbleWords2.txt')
words = whand.read().split('\n')
rhand = open('scrabbleWords2.txt', 'w')
rhand.write((', '.join(words)))
whand.close()
rhand.close()
    
