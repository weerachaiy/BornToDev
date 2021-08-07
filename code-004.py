n = int(input())
for x in range(n-1):
	print("{}{}".format(" "*(n-x-1),"*"*(x+x+1)))
for x in range(n-1,-1,-1):
	print("{}{}".format(" "*(n-x-1),"*"*(x+x+1)))
