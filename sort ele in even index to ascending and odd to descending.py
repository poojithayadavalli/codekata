x=int(input())
y=list(map(int,input().split()))
l=[]
m=[]
n=[]
for i in range(x):
    if i%2==0 or i==0:
        l.append(y[i])
    else:
        m.append(y[i])
l.sort()
m.sort()
h=m[::-1]
for i in range(x//2):
    n.append(str(l[i]))
    n.append(str(h[i]))
if x%2!=0:
    n.append(str(l[len(l)-1]))
print(' '.join(n))
