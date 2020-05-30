n=input().split()
x=int(n[0])
l=[]
count=0
s=list(map(int,input().split()))
for i in s:
    y=i%x
    if y in l:
        count+=1
    else:
        l.append(y)
print(count)
