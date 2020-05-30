n=int(input())
x=input().split()
l=[]
for i in range(n-1):
    for j in range(i+1,n):
        l.append((x[i],x[j]))
print(len(set(l)))
