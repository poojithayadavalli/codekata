import math
m, n = map(int, input().split())
lst = [int(x) for x in input().split()]
for i in range(n):
    a=[]
    l,r = map(int, input().split())
    a=lst[l-1:r]
    ans = a[0]
    for k in range(1, len(a)):
        ans =math.gcd(ans, a[k])
    print(ans)
