def LeapYear(year):
  if year%4 == 0:
    pass
  else:
    return(False)
  if year%100 == 0:
    pass
  else:
    return(True)
  if year%400 == 0:
    return(True)
  else:
    return(False)

year = int(input())
if (LeapYear(year)):
	print("Leap Year")
else:
	print("Not a Leap Year")
