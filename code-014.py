a = []
b = ["THAI","MATH","ENGLISH","SCIENCE","SPORT"]
for x in range(5):
	a.append(float(input()))
for x in range(5):
	print("{} = {}".format(b[x],a[x]))
print("---")
print("GPA = {}".format(sum(a)/len(a)))
