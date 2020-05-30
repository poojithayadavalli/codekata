def reverse(x1):
    x=list(x1[::-1])
    x[0],x[len(x)-1]=x[len(x)-1],x[0]
    return ''.join(x)
n=input().split()
for i in range(len(n)):
    n[i]=reverse(n[i])
print(' '.join(n))
