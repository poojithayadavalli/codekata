x=list(input())
q=int(input())
l=[]
for i in range(q):
  l.append(input().split())
z=""
j=0
while j<3:
  for k in range(int(l[j][1])):
    if l[j][0]=="L":
      temp=x[0]
      for i in range(len(x)-1):
        x[i]=x[i+1]
      x[len(x)-1]=temp
      z+=x[0]
    else:
      temp=x[len(x)-1]
      for i in range(1,len(x)):
        x[i]=x[i-1]
      x[0]=temp
      z+=x[0]
  j+=1
print("Yes"if sorted(x)==sorted(list(z))else "No")
#incomplete
