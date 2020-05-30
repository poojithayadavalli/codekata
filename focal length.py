n=int(input())
l=list(map(int,input().split()))
c=l.copy()
c.sort()
c.reverse()
r=[]
for i in range(len(c)):
    r.append(str(l.index(c[i]))) 
print(" ".join(r))
