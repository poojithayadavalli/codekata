x=int(input())
s=input().split()
l=[]
for i in range(x):
    if(i==int(s[i])):
        l.append(s[i])
l.sort()
print(' '.join(l) if(len(l)) else "-1")
