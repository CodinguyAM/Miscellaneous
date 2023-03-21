
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
  if (month > 12) or (day > 31) or ((day > 30) and (month in [4, 6, 9, 11])) or ((month == 2) and ((day > 29) or ((day > 28) and (not isLeapYear(year))))): return ""
  prevDays = 0
  for prevYear in range(highestMondayStarter(year), year): prevDays = prevDays + dayNum(31, 12, prevYear)
  return prevDays + dayNum(day, month, year)
while True:
  try:
    DAY = int(input("Day of the Month?: "))
    MONTH = int(input("Month?: "))
    YEAR = int(input("Year?: "))
    import time
    from datetime import timedelta
    start_time = time.monotonic()

    print({1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 0:"Sunday", 100:"Sorry"}[absoluteDay(DAY, MONTH, YEAR) % 7])
    print()
    end_time = time.monotonic()
    print(timedelta(seconds=end_time - start_time))
  except: print()

