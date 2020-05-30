n=int(input())
x=input().split()
l=[]
for i in range(0,n-1,1):
    l.append(int(x[i])+int(x[i+1]))
l.sort()
l=l[n-2:]
print(sum(l))
