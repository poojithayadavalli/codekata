def gcd1(m1,n1):
    rem=m1%n1
    if(rem==0):
        return n1
    else:
        return gcd1(n1,rem)
def gcd(m,n,r):
    g=gcd1(m,n)
    h=gcd1(g,r)
    return h
flag=0
s=int(input())
l=[]
while(s>3):
    for i in range(1,s):
        for j in range(i,s-1):
            for k in range(i,s-2):
                if(i+j+k==s and gcd(i,j,k)==1):
                    l.append(i)
                    l.append(j)
                    l.append(k)
                    flag=1
                    break
            if flag==1:
                break
        if(flag==1):
            break
    if(flag==1):
            break
    else:
        break
l=[str(i) for i in l]
l.sort()
print(' '.join(l) if len(l)>0 else "0")
