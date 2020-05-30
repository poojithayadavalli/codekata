n=int(input())
l=[]
for i in range(n):
	x=input()
	l.append(list(x))
p=0
w=0
for j in range(n):
    for k in range(n):
        if(j==0 or j==n-1 or k==0 or k==n-1):
            if(l[j][k]=='#'):
                p+=1
            elif(l[j][k]=='.'):
                w+=1
print(p,end=" ")
print(w)
