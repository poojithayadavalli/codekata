def Triplets(arr,n):
    count=0
    m={}
    m=set()
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (arr[i]<arr[j]and arr[j]<arr[k]):
                    m.add((arr[i],arr[j],arr[k]))
    return len(m)
x=int(input())
y=list(map(int,input().split()))
print(Triplets(y,x))
