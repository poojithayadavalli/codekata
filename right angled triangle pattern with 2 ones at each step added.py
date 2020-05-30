n = int(input())
L = [1]
print(*L)
for i in range(1,n) :
    L = L + [1,1]
    print(*L)
