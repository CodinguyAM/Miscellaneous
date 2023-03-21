class dotTXT:
    def error():
        print("An error occurred.")
    
    
    def __init__(self, string):
        self.text = string
    def write(self, mode, add):
        #e command
        if mode == "-a":
            self.text = self.text + add
        elif mode == "-w":
            self.text = add
        else:
            error()
    def read(self):
        #r command
        print(self.txt)


class Folder:
    txtfile = dotTXT("")
    
    def error():
        print("An error occurred")

    def __init__(self, name, parent=None, contents=None):
        self.name = name
        self.parent = parent
        if self.parent = None:
            self.parent = self
        self.inner = {".." : self.parent}
        if contents != None:
            self.inner = contents
            self.inner[".."] = parent

    def mkdir(self, dirname, content=None):
        newdir = Folder(name=dirname, parent=self, contents=content)

    def d(self, target):
        del self.inner[target]

    def cd(self, target):
        return self.inner[target]

    def mkfile(self, filename, content=""):
        self.inner[filename] = dotTXT(content)

    def e(self, target, mode, add):
        self[target].write(mode, add)

    def ls(self):
        for i in self.inner.keys():
            typ = "Folder"
            if type(self.inner[i]) == type(dotTXT):
                typ = ".txt File"
            print(i, typ)

    def r(self, target):
        self.inner[target] = 

C = Folder(name="C:")
while True:
    userslocation = C
    command = input(userslocation)
    


        
