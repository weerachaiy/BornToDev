def scale(x):
  return((x - min(c))/(max(c) - min(c)))

a = int(input())
b = int(input())
c = []
for x in range(a*b):
    c.append(float(input()))
c = [scale(x) for x in c]
for x in range(a*b):
  print("{:.4f}".format(c[x]), end=" ")
  if (x+1)%a == 0:
    print()
