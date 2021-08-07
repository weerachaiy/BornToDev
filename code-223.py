a = "0123456789"
n = input()
b = "".join([x if x in a  else " " for x in n])
print("{:04d}".format(sum([int(x) for x in b.split()])))
