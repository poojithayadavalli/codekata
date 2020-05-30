n=int(input())
a=list(map(int,input().split()))[:n]
if a[1]!=a[0]+1:
    print(a[0]+1)
elif(a[0]==1):
    print(a[0]+3)
else:
    print(a[0]+2)
