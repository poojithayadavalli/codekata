s=str(input())
r=[]
t=[]
for i in range(len(s)):
    if(s[i] not in r):
        r.append(s[i])
    else:
        t.append(len(r))
        r.clear()
        r.append(s[i]) 
t.append(len(r))
print(max(t))
