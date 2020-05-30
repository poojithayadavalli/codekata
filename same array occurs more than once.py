n=int(input())
l=[]
for i in range(n):
 z=int(input())
 m=list(map(int,input().split()))
 l.append(str(m))
f=0
for i in range(n-1):
 t=l[i+1:n]
 if(l[i] in t):
  f=1
  break
if(f==1):
 print("YES")
else:
 print("NO")
