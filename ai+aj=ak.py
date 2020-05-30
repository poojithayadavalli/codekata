x=int(input())
y=list(map(int,input().split()))
count=0
for i in range(x-2):
    for j in range(i+1,x-1):
        if (y[i]+y[j])in y[j+1:]:
            count+=1
print(count)
