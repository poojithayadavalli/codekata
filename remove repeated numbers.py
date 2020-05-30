x=input().split()
k=x[1]
l=[]
y=input().split()
for i in range(len(y)):
    if y[i]!=k:
    	l.append(y[i])
print(' '.join(l) if len(l) else "empty")
