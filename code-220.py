def piramid(a, y=2, z=0):
    c = len(a)
    b = [a[:x+1] for x in range(c)]
    if z != 0:
        b = [x[1:][::-1]+x for x in b]
    for x in b:
        print(" ".join(list(x)).center(c*y-z))

a = input("")
piramid(a, y=4, z=2)
#piramid(a)
