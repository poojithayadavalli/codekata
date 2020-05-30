def leader(arr,x):
    l=arr[arr.index(x):]
    for i in l:
        if i>x:
            return False
    return True
n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(n-1):
    if leader(arr,arr[i]):
        l.append(arr[i])
l.append(arr[n-1])
y=list(map(str,l))
print(' '.join(y))
