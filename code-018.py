a = int(input())
if a >= 90:
  print("A")
else:
  if a >= 85:
    print("B+")
  else:
    if a >= 80:
      print("B")
    else:
      if a >= 75:
        print("C+")
      else:
        if a >= 70:
          print("C")
        else:
          if a >= 65:
            print("D+")
          else:
            if a >= 60:
              print("D")
            else:
              print("F")
