x = int(input())
n = int(input())
a = []
for y in range(n):
  a.append(input().split())
for y in range(n):
  if x  >= int(a[y][0])  and x <= int(a[y][1]):
    print(a[y][2])
