import operator
l=['A','E','I','O','U','a','e','i','o','u']
x=int(input())
m=[]
for i in range(x):
    m.append(input())
d={}
for i in m:
    d[i]=0
    for j in i:
        if j in l:
            d[i]+=1
h=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
for key in h:
    print(key[0])
