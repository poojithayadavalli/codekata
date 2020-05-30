k=int(input())
l=[]
for i in range(k):
    l.append(input().split())
z=[]
for i in range(k):
    z+=l[i]
y=[int(i)for i in z]
y=sorted(y)
print(*y)
