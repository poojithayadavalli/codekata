s=input().split()
s=''.join(s)
l={}
for i in s:
    if i in l:
        l[i]+=1
    else:
    	l[i]=1
x=min(l.values())
m=[]
for j,k in l.items():
    if k==x:
    	m.append(j)
print(' '.join(m))
