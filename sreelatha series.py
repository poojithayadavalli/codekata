x=int(input())
sum1=0
l=[]
for i in range(x):
    sum1+=(i+1)
    l.append(sum1**2)
print(*l)
