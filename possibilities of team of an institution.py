x,k=map(int,input().split())
y=list(map(int,input().split()))
m=[]
for i in y:
    if i+k<5:
        m.append(str(i))
print(len(m)//2)
