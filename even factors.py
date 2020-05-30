x=int(input())
l=[]
for i in range(1,x+1):
    if x%i==0 and i%2==0:
    	l.append(str(i))
print(' '.join(l))
