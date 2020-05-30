n=int(input())
a=input().split()
b=input().split()
t=0
i=0
while i<n:
    x=a[i]
    for j in range(n-1):
        a[j]=a[j+1]
    a[j+1]=x
    #print(a)
    if ''.join(a)==''.join(b):
        t+=1
        break
    else:
        t+=1
        i+=1
print(t)
