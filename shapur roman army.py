n=int(input())
l=list(map(int,input().split()))
c=0 
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if(l[i]>l[j]>l[k]):
                c=c+1 
print(c)
