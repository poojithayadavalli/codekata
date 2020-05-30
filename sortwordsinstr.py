def rev(s):
    x=list(s)
    x.sort()
    return ''.join(x)
n=input().split()
for i in range(len(n)):
    n[i]=rev(n[i])
print(' '.join(n))
