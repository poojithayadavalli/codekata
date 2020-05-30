x=int(input())
y=input().split()
k=int(input())
c=0
try:
    for i in range(0,x-k+1,k):
        if c%2==0:
            y[i:i+k]=y[i:i+k][::-1]
            c+=1
        else:
            c+=1
            continue
    print(' '.join(y))
except:
    print(' '.join(y))
