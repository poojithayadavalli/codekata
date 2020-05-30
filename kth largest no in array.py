def sort1(h,k):
    x=[]
    for i in h:
        if i in x:
            pass
        else:
            x.append(i)
    x.sort()
    return(x[k-1])
o=int(input())
m=[]
s=[]
y=[]
for i in range(o):
    m.append(input())
    s.append(list(map(int,input().split())))
    y.append(input())
for i in range(o):
    print(sort1(s[i],int(y[i])))
