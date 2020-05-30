n=int(input())
l=list(map(int,input().split()))
t=list(set(l))
r=[]
for i in range(len(t)):
    r.append(l.count(t[i]))
c=0
for i in range(len(l)-1):
    k=0 
    for j in range(len(t)):
        if(l[i]==t[j]):
            k=r[j]
            break 
    if(k==l[i+1]):
        c=c+1 
print(c)
