n,k=map(int,input().split()) 
l=list(map(int,input().split())) 
c=0 
for i in range(len(l)):
    free=86400-l[i]
    k=k-free 
    c=c+1
    if(k<=0):
        break 
print(c)
