n = int(input())
L = [int(x) for x in input().split()]
L2=[]
mx = max(L)
for i in range(n-1) :
    if L[i] > max(L[i+1:]) :
        L2.append(L[i])
L2.append(L[-1])
print(*L2)
print(mx,end='')
