u,v=map(int,input().split()) 
x=u//3
l=[]
if u>0 and u!=v:
    l.append(1)
else:
    l.append(0)
if v<=x:
    l.append(2*v)
else:
    dif=u-v
    l.append(dif)
print(*l)
