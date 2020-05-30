n = int(input())
L = [int(x) for x in input().split()]
L2=[]
for i in range(n) :
    if (i+1)*n in L :
        L2.append(str(i+1))
print(len(L2))
