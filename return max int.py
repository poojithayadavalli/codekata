a,b = [int(x) for x in input().split()]
k = 0
while a > 0 :
    k += 1
    a -= b
print(k,end='')
