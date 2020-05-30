s=int(input())
l=[]
x=[int(i)for i in input().split()]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        l.append(x[i:j+1])
m=[]
for i in l:
    m.append(sum(i))
print(max(m))
