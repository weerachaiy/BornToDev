n = int(input())
a = sorted([int(input()) for x in range(n)], reverse=True)
for x in a:
  print(x)

