C = "kpnbrqKPNBRQ"
D = {"k":0,"p":1,"n":3,"b":3,"r":5,"q":9}
E = {"K":0,"P":1,"N":3,"B":3,"R":5,"Q":9}
A = 0
B = 0
for x in range(8):
  a = [y for y in list(input()) if y in C] 
  for y in a:
    if y in D:
      A = A + D[y]
    if y in E:
      B = B + E[y]
if A-B != 0:
  print(B-A)
else:
  print("equal")
