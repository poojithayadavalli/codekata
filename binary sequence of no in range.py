x=int(input())
l=[]
for i in range(1,x+1):
    b=bin(i)[2:]
    l.append(b)
print(*l)
