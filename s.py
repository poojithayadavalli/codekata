def isprime(n):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            return True
def sumprime(x):
    for i in range(2,int(x)+1):
        if isprime(i):
            s=str(i)
            if s[len(s)-1]=='3':
                return int(s)
print(sumprime(input()))

