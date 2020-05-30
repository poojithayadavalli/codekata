n,k,r=map(int,input().split())
count=0
for i in range(n,k+1):
    if str(r) in str(i):
    	count+=1
print(count)
