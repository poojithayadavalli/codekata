def sumf( a, d,n) : 
    sum1 = 0
    i = 0
    while i < n : 
        sum1 = sum1 + a 
        a = a + d 
        i = i + 1
    return sum1
x,y,k=map(int,input().split())
print(sumf(x,y,k))
