n=int(input()) 
a=list(map(int,input().split())) 
q=int(input()) 
for i in range(q):
    l,r=map(int,input().split()) 
    print(max(a[l-1:r])-min(a[l-1:r])) 
