n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    if i in l:
        pass
    else:
    	l.append(i)
l.sort()
print("-1" if len(l)<2 else l[1])
