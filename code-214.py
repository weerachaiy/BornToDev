# A = N + x
# B = x
# A = N + x - Y
# B = x - Y
# x = (N - Y + M * Y)/(M - 1)
N, M, Y = [int(x) for x in input().split()]
B = N/(M - 1) + Y
A = N + B
print("{} {}".format(int(A),int(B)))
