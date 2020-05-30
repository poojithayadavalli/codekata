x=input()
r="AEIOUaeiou"
l=[]
for i in x:
    if i in r:
        l.append(i)
i=0
m=[]
l.sort()
for j in x:
    if j in r:
        m.append(l[i])
        i+=1
    else:
        m.append(j)
print(''.join(m))
