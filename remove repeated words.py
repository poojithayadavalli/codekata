n=input().split()
x=[]
y=[]
for i in n:
    if i in x:
        pass
        y.append(i)
    else:
    	x.append(i)
for i in y:
    x.remove(i)
print(' '.join(x))
