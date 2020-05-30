x=int(input())
y=list(map(int,input().split()))
for i in range(x-1):
    y[i]=str(max(y[i+1:]))
y[x-1]='0'
print(' '.join(y))
