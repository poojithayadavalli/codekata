x=int(input())
y=list(map(int,input().split()))
l=[]
for i in range(x-1):
    if(y[i]<y[i+1]):
        l.append("0")
    else:
        l.append("1")
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        flag=True
    else:
        flag=False
        break
print("yes" if flag else "no")
