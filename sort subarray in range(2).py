n = int(input())
l = [int(x) for x in input().split()]
a, b = map(int, input().split())
l[a:b+1]=sorted(l[a:b+1])
print(*l)
