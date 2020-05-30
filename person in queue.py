n=int(input())
if n>1:
    b=list(map(int,input().split()))[:n]
    b.sort()
    a=b
    print(b)
    count=0
    for i in range(1,n):
        if a[i]>=a[i-1]:
            count+=1
        a[i]+=a[i-1]
    print(count+1)
