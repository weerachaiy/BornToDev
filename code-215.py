def piramid(a, y=2, z=0):
    c = len(a)
    b = [a[:x+1] for x in range(c)]
    if z != 0:
        b = [x[1:][::-1]+x for x in b]
    for x in b:
        print(" ".join(list(x)).center(c*y-z))

a = int(input())
#piramid(a, y=4, z=2)
#piramid(a)
for y in range(a):
  for x in range(2+y):
    print(("*"*(x+x+1)).center(a*2+1))
print("|".center(a*2+1))
print((("="*a)+"V"+("="*a)).center(a*2+1))
