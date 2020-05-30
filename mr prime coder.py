prime = [2,3,5,7,11,13,17,19]
(r, c) =  map(int, input().split())
l = [[int(x) for x in input().split()] for _ in range(r)]
def isPrime(a):
    f = True
    for i in range(2, a):
        if a % i == 0:
            f = False
            break
    return f
flag = True
s = 0
for i in range(r):
    for j in range(c):
        if (i+j) in prime:
            s += l[i][j]
if isPrime(s):print("YES")
else:print("NO")
