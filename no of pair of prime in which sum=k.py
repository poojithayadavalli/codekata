from itertools import combinations_with_replacement
n=int(input())
prime=[]
for i in range(2,n):
    k=1 
    for j in range(2,i):
        if(i%j==0):
            k=0 
            break 
    if(k==1):
        prime.append(i)
l=list(combinations_with_replacement(prime,2))
c=0
for i in range(len(l)):
    if(sum(l[i])==n):
        c=c+1 
print(c)
