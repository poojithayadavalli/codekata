n=int(input())
for i in range(0,n*n,n):
  if i==0:
    j=1
  else:
    j=i
  print(j**2,end=" ")
#one test
