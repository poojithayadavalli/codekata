def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x: 
            return x
        elif arr[i]<x:
            k=arr[i]
    return k
n,x=map(int,input().split())
arr=list(map(int,input().split()))
print(search(arr,x))
#one
