n=input().split()
s=input().split()
x=int(n[1])
for j in range(x):
    temp=s[len(s)-1]
    for i in range(len(s)-1,-1,-1):
        s[i]=s[i-1]
    s[0]=temp
print(' '.join(s))
# one passed
