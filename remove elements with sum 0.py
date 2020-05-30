x=input()
k=0
z=list(map(int,input().split()))
y=z
m=[]
for i in range(len(y)-1):
    for j in range(i+1,len(y)):
        if y[i]+y[j]==k:
            z.pop(i)
            z.pop(j)
        else:
            pass
print(*z)
    
