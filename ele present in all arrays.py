def intersection(lst1, lst2):
    return [item for item in lst1 if item in lst2]
m,n=map(int,input().split())
l=[]
for i in range(m):
    l.append(list(map(int,input().split())))
x=l[0]
for i in range(1,m):
    x=intersection(x,l[i])
y=list(map(str,x))
print(' '.join(y))
