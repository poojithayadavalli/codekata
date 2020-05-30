n,k=map(int,input().split())
s=input().split()
l=[]
m=[]
for i in range(5):
    l.append(abs(k-int(s[i])))
l.sort()
for i in range(3):
    for j in range(len(s)):
        if(l[i]==abs(k-int(s[j]))):
            m.append(s[j])
print(' '.join(s))
            ##not solved
