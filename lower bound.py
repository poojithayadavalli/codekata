n,k=map(int,input().split())
l=list(map(int,input().split()))
result=0
for i in range(0,len(l)):
  if(l[i]==k):
    print(k)
    exit()
difference=[]
for i in range(0,len(l)):
  if(l[i]<k and l[i]>result):
      result=l[i]
print(result)
