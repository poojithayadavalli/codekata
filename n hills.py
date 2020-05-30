import math
n=int(input()) 
a=list(map(int,input().split())) 
q=int(input()) 
for _ in range(q):
    l,r=map(int,input().split()) 
    t=a[l-1]
    f=1
    for i in range(l,r):
        if(a[i]>t):
            f=0 
            break 
    if(f==1):
        print("YES") 
    else:
        print("NO")
