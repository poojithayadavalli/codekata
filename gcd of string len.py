def gcd(a,b):
    if a%b==0:
    	return b
    elif b%a==0:
    	return a
    elif a<b:
    	return gcd(a,b%a)
    else:
    	return gcd(b,a%b)
x=input().split()
a=len(x[0])
b=len(x[1])
if gcd(a,b)==1:print("yes")
else:print("no")
