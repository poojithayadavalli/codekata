n,x=map(int,input().split())
y=list(map(int,input().split()))
count=0
for i in range(len(y)-1):
    for j in range(i+1,len(y)):
        if abs(y[i]-y[j])==x:
            count+=1
print(count)
    
