n = int(input())
l = [int(x) for x in input().split()]
q = int(input())
for i in range(q):
    (op, x, y) = map(int, input().split())
    if op == 1:
        for i in range(x, y+1):
            if l[i-1] == 0:l[i-1] = 1
            else:l[i-1] = 0
    if op == 2:
        print(sum(l[x-1:y]))
