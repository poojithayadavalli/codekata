n=int(input())
x=[]
y=input().split()
for i in range(1,n+1):
	x.append(str(i))
for j in x:
    if j not in y:
    	print(j)
