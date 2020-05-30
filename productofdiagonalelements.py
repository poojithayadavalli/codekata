n=int(input())
l=[]
sum1=1
sum2=1
for i in range(n):
    l.append(input().split())
for i in range(n):
    for j in range(n-i-1,-1,-1):
        sum1=sum1*int(l[i][i])
        sum2=sum2*int(l[j][i])
        break
print(sum1+sum2)
