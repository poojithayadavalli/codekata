n,k=map(int,input().split()) 
l=list(map(int,input().split())) 
r=[]
while (l.count(k)): 
    l.remove(k)  
for i in range(len(l)):
    r.append(abs(l[i]-k))
t=[]
for i in range(3):
    t.append(str(l[r.index(min(r))])) 
    l.remove(l[r.index(min(r))])
    r.remove(min(r))
print(" ".join(t))
