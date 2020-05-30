n=int(input())
s=input().split()
l=[]
for i in range(len(s)):
    for j in range(len(s)):
        if(s[i]<s[j]):
            l.append((i,j))
x=set(l)
print(len(x))
