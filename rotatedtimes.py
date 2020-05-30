n,k=map(int,input().split())
s=input().split()
for m in range(k):
    temp=s[0]
    for i in range(len(s)-1):
        s[i]=s[i+1]
    s[len(s)-1]=temp
print(''.join(s))
