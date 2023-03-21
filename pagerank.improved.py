#pageRank sumlator!!
# note: $ at the end of a comment means cont. comment with $ at start
# Page class
class Page:
    def __init__(self, outgoingLinks, numPages):
        self.rank = 1/numPages
        self.prevRank = -1000
        self.oL = outgoingLinks
    def outflow(self):
        out = {}
        #for every outgoing link, $
        for oL in self.oL:
            #$apportion an equal part of the pageRank
            out[oL] = self.rank/len(self.oL)
        return out
    def update(self, amoDic):
        self.prevRank = self.rank
        self.rank = 0
        for page in amoDic.keys():
            self.rank = self.rank + amoDic[page]
    def isStable(self):
        return abs(self.rank - self.prevRank) < 1/25
class Web:
    def __init__(self, linksDic):
        self.links = linksDic
        self.pages = list(linksDic.keys())
        self.pageObjs = {}
        for p in self.pages:
            #
            self.pageObjs[p] = (Page(self.links[p], len(self.pages)))
    def update(self):
        for p in self.pageObjs.values():
            print(p.rank)
            print(p.prevRank)
            print(p.oL)
        outflows = {}
        for page in self.pages:
            outflows[page] = self.pageObjs[page].outflow()
        inflows = {}
        for page in self.pages:
            inflowdic = {}
            for opage in self.pages:
                if page in outflows[opage].keys():
                    inflowdic[opage] = outflows[opage][page]
            inflows[page] = inflowdic
        for pageOb in self.pageObjs.keys():
            pageObj = self.pageObjs[pageOb]
            pageObj.update(inflows[pageOb])

    def isStable(self):
        i =0
        isStabl = True
        while isStabl and i < len(self.pageObjs.values()):
            isStabl = self.pageObjs[self.pages[i]].isStable()
        return isStabl



            
            
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    if True:
        LD = {}
        numPages = int(input("Hi! How many pages will be in your web?: "))
        for i in range(numPages):
            p = a[i]
            linksOfP = input("What pages does page "+ p +" link to?: ")
            LD[p] = linksOfP
        print(LD)
        web = Web(LD)
        while not web.isStable():
            print("at next upd")
            web.update()
            print("updae finishies")
            for page in web.links.keys():
                print(page, "has", web.pageObjs[page].rank, "units of pageRank")
                print("That's", web.pageObjs[page].rank * 100, "percent!")
                print()
                print()
##    except KeyboardInterrupt:
##        break
##    except:
##        print()
