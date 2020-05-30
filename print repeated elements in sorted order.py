x=input()
y=input().split()
l=[]
m=[]
for i in y:
    if i in l:
        m.append(i)
    else:
        l.append(i)
m.sort()
n=set(m)
print(' '.join(n)if len(n) else "unique")
