a = []
while(True ):
	n = input()
	if n.upper() == "MAX":
		break
	if n.upper() == "MIN":
		break
	a.append(int(n))
a.remove(0)
if n.upper() == "MAX":
	print("{}".format(" ".join([str(x) for x in sorted(a, reverse=True)])))
if n.upper() == "MIN":
	print("{}".format(" ".join([str(x) for x in sorted(a, reverse=False)])))
