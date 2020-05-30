def gcd(a,b):
    if a == 0:
        return b
    if b>a:
    	return gcd(b%a,a)
    else:
    	return gcd(a%b,b)
n=int(input())
s=input().split()
g1=int(s[0])
for i in s[1:]:
    g1=gcd(g1,int(i))
print(g1)
    
