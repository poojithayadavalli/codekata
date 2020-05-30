n=int(input())
for i in range(n//2):
  if 2**i==n:
    print("yes")
    break
else:
  print("no")
