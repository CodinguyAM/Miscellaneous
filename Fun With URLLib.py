import urllib.request

#these are not allowed in words - <>=#)($._
proh = '/<>=#)($._0123456789\|[]{}:;'
def allnotin(s, p):
    for c in p:
        if c in s:
            return False
    return True
while True:
    URL = input("Enter your URL: ")
    fhand = urllib.request.urlopen(URL)
    counts = dict()
    maxLen = 0
    listen = False
    actualText = []
    for line in fhand:
        words = line.decode().split(" ")
        for word in words:
            if len(word) > 0:
                if allnotin(word, proh):
                    #print("yes")
                    actualText.append(word.strip())
            else:
                #print("no")
                pass
            if len(word) == 0:
                continue
            if len(word) > 3:
                if word[:4] == "<div":
                    listen = True
            if len(word) > 1:
                if word[:2] == "<p":
                    listen = True
            if "</div>" in word or "</p>" in word:
                listen = False

    for word in actualText:
        if word in counts.keys():
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    def findfreq(word):
        global counts
        return counts[word]

    sorted_words = list(counts.keys())
    sorted_words.sort(key=findfreq, reverse=True)
    print("The frequencies are, ")
    for w in sorted_words:
        print(w + ((maxLen - len(w)) * " "), findfreq(w))
