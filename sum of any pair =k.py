n,k=map(int,input().split())
x=list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        if x[i]+x[j]==k:
            flag=True
            break
        else:
            flag=False
    if flag:
        break
print("yes" if flag else"no")
        
