x=int(input())
def fact(n):
    if n==0 or n==1:
        return 1
    else:
    	return n*fact(n-1)
n=2*x
y=(fact(n)//(fact(n-x)*fact(x)))
print(y//x+1)
