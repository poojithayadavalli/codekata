n=int(input())
l=list(map(int,input().split()))
result=[]
for i in range(n):
  t=bin(l[i])
  c=0
  for j in range(len(t)):
    if(t[j]=="1"):
      c=c+1
  result.append(c)
for i in range(n):
  if(i==n-1):
    print(l[result.index(max(result))])
    l.remove(l[result.index(max(result))])
    result.remove(max(result))
  else:
    print(l[result.index(max(result))],end=" ")
    l.remove(l[result.index(max(result))])
    result.remove(max(result))
