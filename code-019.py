def grade(a):
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

a = "Error : Value must be less than or equal to 100."
b = "Error : Value must be greater than or equal to 0."
n = int(input())
if n >100:
  print(a)
else:
  if n < 0:
    print(b)
  else:
    grade(n)
