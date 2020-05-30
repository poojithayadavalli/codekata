def prime(m,n):
    l=[]
    for k in range(m,n):
        if(k==2):
            l.append(str(k))
        for i in range(2,k):
            if(k%i==0):
                break
            else:
                l.append(str(k))
                break
    return l
n=int(input())
x=[]
for i in range(n):
    x.append(input().split())
for i in range(n):
    print(len(prime(int(x[i][0]),int(x[i][1]))))
