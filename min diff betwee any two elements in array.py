x=int(input())
y=list(map(int,input().split()))
m=[]
for i in range(x-1):
    for j in range(i+1,x):
        m.append(str(abs(y[i]-y[j])))
print(min(m))
    
