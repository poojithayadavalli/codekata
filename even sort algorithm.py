n=int(input())
m=list(map(int,input().split())) 
l=[]
for i in range(0,len(m)):
  l.append(i)
def evensort(length,l):
  if(length==1):
    return l[0]
  else:
    t=[]
    for i in range(0,len(l)):
      if((i+1)%2==0):
        t.append(l[i])
    return evensort(len(t),t) 
print(evensort(len(l),l))
