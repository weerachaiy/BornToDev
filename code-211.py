a = input()
while len(list(a)) > 1:
  a = str(sum([int(x) for x in list(a)]))
print(a)
