n,k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
L2 = sorted(L[:k]) + sorted(L[k:],reverse=True)
print(*L2,end='')
