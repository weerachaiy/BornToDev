def isPassword(password):
  l = [x for x in list(password) if x in ls]
  u = [x for x in list(password) if x in us]
  n = [x for x in list(password) if x in ns]
  if len(password) >= 3 and len(password) <= 20 and len(l) > 0 and  len(u) > 0 and  len(n) > 0:
    print("Valid")
  else:
    print("Invalid")
  
ls = "abcdefghijklmnopqrstuvwxyz"
us = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ns = "0123456789"
password = input()
isPassword(password)

