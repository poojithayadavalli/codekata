x=int(input())
y=[int(i) for i in input().split()]
def so(y):
    l=[i for i in y if y.index(i)%2==0]
    m=[i for i in y if y.index(i)%2!=0]
    l.sort()
    n=[]
    for j in range(min(len(l),len(m))):
    	n.append(l[j])
    	n.append(m[j])
    if len(y)%2!=0:
    	n.append(l[len(l)-1])
    return n
m=so(y)
print(*m)
    	
