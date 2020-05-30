def isprime(x):
    if x==2:
        return True
    else:
        for j in range(2,x):
            if(x%j)==0:
                flag=False
                break
            else:
                flag=True
        return flag
n=int(input())
l=[]
m=[]
for i in range(2,n+1):
    if n%i==0:
    	l.append(str(i))
for j in l:
    if isprime(int(j)):
    	m.append(j)
m.sort()
print(' '.join(m))
