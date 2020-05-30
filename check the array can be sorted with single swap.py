n=int(input())
s=[int(x) for x in input().split()]
l=sorted(s)
for i in range(n):
    if(l[i]!=s[i]):
        s[i],s[i+1]=s[i+1],s[i]
        if l==s:
            print(i)
            flag=False
            break
        else:
            print("-1")
            flag=True
            break
    else:
        flag=True
if flag: print("-1")
