x=int(input())
y=input().split()
l=[]
for i in y:
    for t in range(int(i)):
        if int(i)==(t**3)+((t+1)**3):
            l.append(i)
            break
l1=list(map(int,l))
l1.sort()
l2=list(map(str,l1))
print(' '.join(l2) if len(l1) else "-1")
#incomp
