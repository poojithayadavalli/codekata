def findMaximum(arr, low, high): 
    max1 = arr[low] 
    i = low 
    for i in range(high+1): 
        if arr[i] > max1: 
            max1 = arr[i] 
    return max1
x=int(input())
arr=list(map(int,input().split()))
print(findMaximum(arr,0,x-1))
