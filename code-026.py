n = int(input())
for x in range(n):
	print("{}{}".format(" "*(n-x-1),"*"*(x+x+1)))
