x=int(input())
y=input().split()
k=int(input())
for i in range(0,x-k+1,k):
    y[i:i+k]=y[i:i+k][::-1]
print(' '.join(y))
