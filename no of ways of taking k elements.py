def fact(n):
    p=1
    for i in range(1,n+1):
        p *= i
    return p
n,k = [int(x) for x in input().split()]
ans = fact(n)//fact(n-k)
print(ans,end='')
