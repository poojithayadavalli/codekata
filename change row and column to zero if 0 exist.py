import sys, copy
m,n = [int(x) for x in input().split()]
L = []
for i in range(m) :
    L2 = [int(x) for x in input().split()]
    L.append(L2)
L3 = copy.deepcopy(L)
for i in range(m) :
    for j in range(n) :
        if L[i][j] == 0 :
            for k in range(m) :
                L3[k][j] = 0
            for k in range(n) :
                L3[i][k] = 0
for i in range(m-1) :
    print(*L3[i])
print(*L3[m-1],end='')
