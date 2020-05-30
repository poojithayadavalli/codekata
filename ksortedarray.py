n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(input().split())
    l[i].sort()
x=l[0]
for i in range(1,len(l)):
    x=x+l[i]
print(' '.join(x))
