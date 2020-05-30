x=int(input())
y=input().split()
l=[]
h=len(y)
while h>0:
    l.append(y[(h-1)//2])
    y.remove(y[(h-1)//2])
    h=len(y)
print(' '.join(l))
