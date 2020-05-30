s=int(input())
x=list(map(int,input().split()))
l=[]
for i in range(s):
    if (i%2==0 and x[i]%2==1)or(i%2==1 and x[i]%2==0):
        l.append(x[i])
print(*l if len(l) else"-1")
