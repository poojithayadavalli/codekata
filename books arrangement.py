x=int(input())
m=input().split()
y=int(input())
n=input().split()
l=[]
for i in n:
    for j in m:
        if j<i:
            l.append(str(m.index(j)+1))
            break
print(' '.join(l))
    
    
