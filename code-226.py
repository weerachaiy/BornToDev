n = int(input())
a = []
for x in range(n):
  a.append(input())
f = input()
b = [True if x == f else False for x in a]
c = [str(x+1) for x in range(len(b)) if b[x] == True]
print("Position: {}".format(",".join(c)))
