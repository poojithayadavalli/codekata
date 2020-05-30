x=int(input())
y=list(map(int,input().split()))
sum1=max(y)
for i in range(x-1):
    for j in range(i+1,x):
        if(abs(y[i]+y[j])<sum1):
            sum1=abs(y[i]+y[j])
            m=y[i]
            n=y[j]
print(m,n)
        
