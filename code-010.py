n = 5
a = ["$"*(x+1) for x in range(n)]
for x in range(n):
	print("{}{}".format(" "*(n-x-1)," ".join(list(a[x]))))
