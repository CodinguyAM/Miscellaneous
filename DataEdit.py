class Table:
    def __init__(self, columns, rows, col_names):
        self.data = {}
        cur_id = 0
        for n in range(rows):
            row = []
            for m in range(columns):
                row.append(None)
            self.data[cur_id] = row
            cur_id = cur_id + 1
        self.columns = col_names
        self.cur_id = cur_id
    def findr(self, column, value):
        res = []
        for rownum in range(len(self.data)):
            row = self.data[rownum]
            if row[column] == value:
                res.append(rownum)
        return res
    def find(self, column, value):
        res = []
        for n in self.findr(column, value):
            res.append(self.data[n])
        return res
    def set_to(self, column, rowid, value):
        self.data[rowid][column] = value
    def view(self, rows=self.data):
        print(self.columns)
        for row in rows:
            print(self.data[row])
    def addrow(self, row):
        self.cur_id = self.cur_id + 1
        self.data[cur_id] = row
    def view_id(self, rows)
def parse(code):
    global curdbs
    lines = code.split(";")
    for line in lines:
        words = line.split()
        first = words[0]
        if first == "REGISTER":
            num = len(words) - 2
            cols = "["
            for word in words[3:]:
                cols = cols + word
            cols = cols + "]"
            com = words[1] + " = Table(" + words[1] + ", " + num + ", " + words[2] + ", " + cols + ")"
            exec(com)
        if first = "ADD":
             


        
