n=int(input())
s=input().split()
for j in range(0,n-1,2):
    for i in range(0,n-1,2):
        if(s[i+2]<s[i]):
            s[i+2],s[i]=s[i],s[i+2]
print(' '.join(s))
