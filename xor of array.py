def pairORSum(arr, n) : 
    ans = 0
    for i in range(0, n) :
        for j in range(i + 1, n) :
            ans = ans + (arr[i] ^ arr[j]) 
    return ans 
x=input()
arr=list(map(int,input().split()))
n = len(arr)
print(pairORSum(arr, n)) 
