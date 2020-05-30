n,k = [int(x) for x in input().split()]
L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]
L3 = []
for x in L2 :
    L1.append(x)
    L3.append(max(L1))
print(*L3,end='')
