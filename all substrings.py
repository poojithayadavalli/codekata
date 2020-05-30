t,n=input().split()
n=int(n)
res=[t[i: j] for i in range(len(t))for j in range(i + 1, len(t) + 1)]
l=[]
print(res)
for i in res:
    if len(i)==n:
        l.append(i)
print(' '.join(l))
