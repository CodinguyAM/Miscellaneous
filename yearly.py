def isLeapYear(year):
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0: return True
      return False
    return True
  return False
def dayNum_(day, month):
  return day + {1:0, 2:31, 3:60, 4:91, 5:121, 6:152, 7:182, 8:213, 9:244, 10:274, 11:305, 12:335}[month]
def dayNum(day, month, year): return dayNum_(day, month) - int((month > 2) and (not (isLeapYear(year))))
def highestMondayStarter(y):
  curYear = y
  while True:
    if (((curYear - 1703) % 400) == 0) or (((curYear - 1900) % 400) == 0) or (((curYear - 2091) % 400) == 0): return curYear
    curYear = curYear - 1
def absoluteDay(day, month, year):
  if month > 12: return ""
  prevDays = 0
  for prevYear in range(highestMondayStarter(year), year): prevDays = prevDays + dayNum(31, 12, prevYear)
  return prevDays + dayNum(day, month, year)
MONTHS = ["", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
while True:
  try:
    YEAR = int(input("Year?: "))
    for MONTH in range(1, 13):
      ML = ["", 31, 28 + int(isLeapYear(YEAR)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      linstartday = ((absoluteDay(1, MONTH, YEAR) - 1) % 7)
      startDay = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}[linstartday]
      print(" "*7, MONTHS[MONTH], YEAR)
      print("MON TUE WED THU FRI SAT SUN")
      for i in range(linstartday):
        print(" "*3, end=" ")
      i = linstartday
      day = 1
      while day <= ML[MONTH]:
        if i == 6:
          print(str(day) + (" " * (3 - len(str(day)))))
          i = 0
        else:
          print(str(day) + (" " * (4 - len(str(day)))), end="")
          i = i + 1
        day = day + 1
      print("\n")
  except:
    pass