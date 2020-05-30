def fact(n) :
    p=1
    for i in range(2,n+1) : p *= i
    return p

n,k = [int(x) for x in input().split()]
res = fact(k)
print(res,end='')
