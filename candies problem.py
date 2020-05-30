def candies(n, arr):
    dp =[1]*n
    for i in range(1,n):
            if arr[i] > arr[i-1]:
                dp[i] = dp[i]+dp[i-1]
    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1] and dp[i] <= dp[i+1]:
            dp[i]= dp[i+1]+1
    return sum(dp)
n=int(input())
arr=list(map(int,input().split()))
print(candies(n,arr))
