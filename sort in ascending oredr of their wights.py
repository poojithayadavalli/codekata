import operator
n=int(input())
x=input().split()
y=input().split()
z={}
l=[]
for i in range(n):
    z[x[i]]=int(y[i])
h=sorted(z.items(),key=operator.itemgetter(1))
print(h)
for key in h:
    l.append(key[0])
print(' '.join(l))

