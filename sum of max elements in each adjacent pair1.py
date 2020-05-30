n=int(input())
x=input().split()
l=[]
for i in range(0,n-1,1):
    l.append([int(x[i]),int(x[i+1])])
sum1=0
for i in l:
    sum1+=max(i)
print(sum1)
