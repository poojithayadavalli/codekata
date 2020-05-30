n=input().split()
k=int(n[1])
for i in range(k-1,len(n[0])-k+2,k-1):
  print(n[0][i],end=" ")
