import sys
def minDist(L, n, u, v) :
    i, j = 0,0
    min1 = sys.maxsize
    for i in range(0,n-1) :
        for j in range(i+1, n) :
            if( (u==L[i] and v==L[j] or v==L[i] and u==L[j]) and \
                            min1 > abs(i-j)) :
                min1 = abs(i-j)

    return min1

n = int(input())
L = [int(x) for x in input().split()]
u,v = [int(x) for x in input().split()]
res = minDist(L, n, u, v)
print(res,end='')
