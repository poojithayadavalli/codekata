n=int(input())
l=list(map(str,input().split()))
t=[]
for i in range(len(l)):
    t.append(len(l[i]))
t=list(set(t))
r=[]
for i in range(len(t)):
    m=[]
    r.append(m) 
for i in range(len(l)):
    for j in range(len(t)):
        if(len(l[i])==t[j]):
            r[j].append(l[i]) 
for i in range(len(r)):
    r[i].sort() 
t=[]
for i in range(len(r)):
    t=t+r[i]
print(" ".join(t))
