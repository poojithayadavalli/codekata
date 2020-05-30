def binarySearch (arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return mid
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1
n,k=map(int,input().split())
s=list(map(int,input().split()))
print("Yes" if binarySearch(s,0,1,k)!=-1 else "No")
