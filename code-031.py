n = int(input())
a = []
for x in range(n):
	a.append(int(input()))
for x in range(n-1, -1, -1):
	print(a[x])
