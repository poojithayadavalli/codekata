x=int(input())
y=input().split()
z=list(y)
z.sort()
m=z[::-1]
l=[]
for i in m:
    l.append(str(y.index(i)))
print(' '.join(l))
