def gcd(x,y):
    a=int(x)
    b=int(y)
    if a == 0:
        return b
    return gcd(b%a,a)
n=input().split()
s=input().split()
s1=[]
for i in range(int(n[1])):
    s1.append(input().split())
for i in range(int(n[1])):
    print(gcd(s1[i][0],s1[i][1]))
