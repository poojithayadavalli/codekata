x=int(input())
y=input().split()
l=[]
sum1=int(y[0])
l.append(y[0])
for i in range(1,x):
    if int(y[i])%2==0:
    	sum1+=int(y[i])
    	l.append(str(sum1))
    else:
    	sum1+=int(y[i])
    	l.append(y[i])
print(' '.join(l))
