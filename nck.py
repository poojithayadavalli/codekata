def fact(n):
    if n==0 or n==1:
        return 1
    else:
    	return n*fact(n-1)
n1=input().split()
n=int(n1[0])
k=int(n1[1])
if(n<=k):
    print(fact(n)//(fact(n-k)*fact(k)))
