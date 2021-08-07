n = int(input())
for x in range(n):
  if x == 0 or x == n-1:
    print("{}".format("#"*n))
  if x > 0 and x < n-1:
    print("#{}#".format(" "*(n-2)))
