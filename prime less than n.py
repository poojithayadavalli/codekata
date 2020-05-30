def isprime(n):
    flag=True
    if n>1:
        if n==2:
            return True
        else:
            for j in range(2,n-1):
                if n%j==0:
                    flag=False
                    break
            return flag
n=int(input())
a=[]
for i in range(n):
    if isprime(i):
        a.append(i)
print(*a)
