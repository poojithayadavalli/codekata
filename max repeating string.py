x=input().split()
x.sort()
count=0
for i in x:
    if x.count(i)>count:
        count=x.count(i)
        m=i
print(m,i,sep=" ")
