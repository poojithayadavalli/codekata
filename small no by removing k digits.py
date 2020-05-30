from itertools import combinations
n,d=map(str,input().split())
d=int(d)
n=list(n)
m=list(combinations(n,len(n)-d))
r=[]
for i in range(len(m)):
    t="".join(m[i])
    r.append(int(t))
print(min(r))
