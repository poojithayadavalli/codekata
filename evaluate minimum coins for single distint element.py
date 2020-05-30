x=int(input())
y=list(map(int,input().split()))
m=max(y)
y.remove(m)
print(sum(y))
#incomplete
