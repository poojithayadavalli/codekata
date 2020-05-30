x=int(input())
y=input().split()
emp=[]
sal=[]
for i in range(len(y)):
    if i%2==0:
        emp.append(y[i])
    else:
        sal.append(y[i])
m=list(sal)
m.sort()
for i in m:
    print(y[y.index(str(i))-1])

