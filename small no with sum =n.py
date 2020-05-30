x=int(input())
l=[]
if x>9:
    for i in range(x):
        for j in range(x):
            if i+j==x:
                l.append(str(i)+str(j))
else: l.append(x)
l=list(map(int,l))
print(min(l))
