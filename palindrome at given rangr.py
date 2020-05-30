s=str(input())
s=list(s)
n=int(input())
x=[]
for i in range(n):
    l,r=map(int,input().split())
    t=s[l-1:r]
    c=t.copy()
    c=c[::-1]
    if(t==c):
        x.append("YES")
    else:
        x.append("NO")
for i in range(len(x)):
    print(x[i])
