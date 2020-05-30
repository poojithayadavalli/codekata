s = input()
n = len(s)
L=[]
i=0
while i < n :
    c = s[i]
    k=0
    while i < n and c==s[i] :
        k += 1
        i += 1
    L.append(c)
    L.append(str(k))

res = ''.join(L)
print(res,end='')
