def isprime(x):
    if x>1:
        if x==2:
            return True
        flag=True
        for i in range(2,x):
            if x%i==0:
                flag=False
                break
        return flag
    else:
        return False
def sum1(x):
    s=0
    for i in x:
        s+=int(i)
    return s
m,r=map(int,input().split())
l=[]
for i in range(m,r+1):
    if len(str(i))==1:
        if isprime(i):
            l.append(i)
    else:
        if isprime(sum1(str(i))):
            l.append(i)
print(*l)
