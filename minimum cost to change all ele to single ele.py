x=int(input())
y=[int(i)for i in input().split()]
l=[]
z=y
for i in y:
    z.remove(i)
    l.append(sum(z))
    z.append(i)
    z.sort()
    #print(z)
print(min(l))
