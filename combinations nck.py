def fact(n):
    if n==0 or n==1:
        return 1
    else:
    	return n*fact(n-1)
n,k=map(int,input().split())
r=fact(n)//(fact(n-k)*fact(k))
print(r)
