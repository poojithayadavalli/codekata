x=int(input())
y=input().split()
m=int(input())
l=[]
for i in y:
    if int(i)%m==0:
    	l.append("1")
    else:
    	l.append("0")
print(' '.join(l))
