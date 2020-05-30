def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif b>a:
    	return gcd(b%a,a)
    else:
    	return gcd(a%b,b)
def stiff(x):
    for i in range(x-1):
        for j in range(i,x):
            if gcd(i,j)==1:
                return True
m=int(input())
if(stiff(m)):
    print("Stiff")
else:
    print("Not stiff")
#incomplete
