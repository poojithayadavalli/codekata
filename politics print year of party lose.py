import operator
n=int(input())
x=input().split()
y=input().split()
z={}
l=[]
for i in range(n):
    z[x[i]]=y[i]
h=sorted(z.items(),key=operator.itemgetter(0))
p={}
for i in range(n):
    if y[i] in p:
        p[y[i]]+=1
    else:
        p[y[i]]=1
for j,k in p.items():
    if
#incomplete

