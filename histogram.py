def copylist(l):
  L = []
  for n in l:
    L.append(n)
  return L


def removeall(l, x):
  while (l.count(x) > 0):
    l.remove(x)
  return l
def abovex(data, x):
  count = 0
  for num in data:
    if num > x:
      count = count + 1
  return count

def belowx(data, x):
  count = 0
  for num in data:
    if num < x:
      count = count + 1
  return count

def avg(data):
  return sum(data)/len(data)

def gmean(data):
  i = 1
  for num in data:
    i = i * num
  return i ** (1/len(data))

def mode(data):
  curmode = None
  maxocc = 0
  for num in set(data):
    if data.count(num) >= maxocc:
      maxocc = data.count(num)
      curmode = num
  return curmode

def median(data):
  for num in data:
    if abovex(data, num) == belowx(data, num):
      return num


def variance(data):
  mean = avg(data)
  sqdists = []
  for num in data:
    sqdists.append((num - mean) ** 2)
  return avg(sqdists)


def stddev(data):
  return variance(data) ** 0.5


def histogram(data):
  counts = {}
  for num in data:
    try:
      counts[num] = counts[num] + 1
    except:
      counts[num] = 1
  printlist = []
  numlist = set(data)
  addstr = " |"
  for num in numlist:
    addstr = addstr + str(num) + " "
  printlist.append(addstr)
  printlist.append("__" + "_" * (len(addstr) - 2))
  for n in range(1, max(counts.values()) + 1):
    addstr = " |"
    for num in numlist:
      numlen = len(str(num))
      if numlen % 2 == 0:
        begstr = " "* int(((numlen-2)/2))
        endstr = " "* int(((numlen)/2))
      else:
        begstr = " "* int(((numlen-1)/2))
        endstr = " "* int(((numlen-1)/2))

      if counts[num] >= n:
        midstr = "O"
      else:
        midstr = " "
      addstr = addstr + begstr + midstr + endstr + " "
    printlist.append(addstr)
  for line in printlist[::-1]:
    print(line)
      


while True:
  data = input("Enter numerical data (separate by commas no spaces): ").split(",")
  print("Histogram")
  histogram(data)
  print()
