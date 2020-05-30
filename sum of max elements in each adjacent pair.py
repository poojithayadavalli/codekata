n=int(input())
x=input().split()
l=0
for i in range(n-1):
    l+=int(max([x[i],x[i+1]]))
    print(l)
l+=int(max([x[0],x[n-1]]))
print(l)
