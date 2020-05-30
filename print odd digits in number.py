x=input()
l=[]
for i in x:
    if int(i)%2==1:
    	l.append(i)
print(' '.join(l) if len(l) else "-1")
