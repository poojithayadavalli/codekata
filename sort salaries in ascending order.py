x=int(input())
y=list(map(int,input().split()))
y.sort()
z=list(map(str,y))
print(' '.join(z))
