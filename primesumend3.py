def isprime(n):
    flag=True
    if n==2:
        flag=True
    else:
        for i in range(2,n):
            if n%i==0 :
                flag=False
    return flag
def sumprime(x):
    l=[]
    for i in range(2,int(x)+1):
        if isprime(i):
            s=str(i)
            if s[len(s)-1]=='3':
                l.append(s)
    return l
x=input()
if int(x)>2:
    l=sumprime(x)
s1=0
for i in range(len(l)):
    s1+=int(l[i])
print(s1)
