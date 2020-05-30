x=int(input())
y=list(map(int,input().split()))
l=[]
for i in range(1,x+1):
    l.append(str(i))
m=list(map(int,l))
m.sort()
if m==y:
    print("yes")
else:
    print("no")
