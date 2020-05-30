sum1=1000
l=[]
l.append(sum1)
x=int(input())
if x==1:
    l.append(1000)
else:
    l.append(1000)
    for i in range(2,x+1):
        sum1=l[i-1]+l[i-2]
        l.append(sum1)
print(sum(l))
