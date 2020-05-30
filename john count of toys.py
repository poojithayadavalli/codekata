n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l.sort()
y=0
count=0
while True:
    while y<n:
        if l[y]<k:
            k=k-l[y]
            y+=1
            count+=1
        else:
            y=n
    if y==n:
        break
print(count)
