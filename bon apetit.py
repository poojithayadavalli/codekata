n,index=map(int,input().split())
l=list(map(int,input().split()))
charged=float(input())
actual=float(0)
for i in range(0,len(l)):
  if(i!=index):
    actual=actual+(float(l[i])/float(2))
if(charged-actual==float(0)):
  print("Bon Appetit")
else:
  print(int(charged-actual))
