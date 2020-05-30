n,m=map(int,input().split())
l=list(map(str,input().split()))
r=[]
t=len(l)-1
for i in range(m):
    if(t==-1):
        break
    r.append(l[t])
    t=t-1
r.reverse()
print(" ".join(r))
