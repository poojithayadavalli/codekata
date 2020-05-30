n=input().split()
for i in range(1,len(n)-1):
    if n[i]=="and":
    	n[i-1],n[i+1]=n[i+1],n[i-1]
print(' '.join(n))
