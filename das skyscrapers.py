z=int(input())
for _ in range(z):
    n=int(input()) 
    l=list(map(int,input().split())) 
    l.reverse()
    c=1 
    t=l[0]
    for i in range(1,len(l)):
        if(l[i]>t):
            c=c+1 
            t=l[i] 
    print(c)
