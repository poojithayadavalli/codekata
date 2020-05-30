n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    if i in l:
        pass
    else:
    	l.append(i)
l.sort()
print(l[len(l)-2])
