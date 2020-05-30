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
x=int(input())
l=[]
for i in range(2,x**2):
    if len(str(i))>1:
        for j in range(len(str(i))):
            if isprime(int(str(i)[j])):
                flag=True
            else:
                flag=False
                break
        if flag:
            l.append(i)
    else:
        if isprime(i):
            l.append(i)
#print(l)
print(l[x-1])
