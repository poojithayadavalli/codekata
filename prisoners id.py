x=int(input())
s=input().split()
l=[]
for i in set(s):
    if s.count(i)>1:
        l.append(i)
print(*l if len(l)else "-1")
