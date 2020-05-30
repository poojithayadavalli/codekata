x=int(input())
y=list(map(int,input().split()))
sum1=0
for i in range(x-1):
    sum1+=(y[i]+y[i+1])
print(sum1)
