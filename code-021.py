name = input()
year = int(input())
age = 2021 - year
if age >= 18:
	print("Welcome {} to NongGipsy Pub".format(name))
else:
	print("You shall not pass!")
