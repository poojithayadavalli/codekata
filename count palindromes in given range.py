x=int(input())
l=[]
for i in range(x):
    t=str(i)[::-1]
    if t==str(i):
        l.append(str(i))
print(len(l))
