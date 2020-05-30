n=int(input())
x=[]
for i in range(n):
    x.append(list(input()))
    x[i].sort()
y=['k','a','b','a','l','i']
y.sort()
count=0
for i in range(n):
    if x[i]==y:
    	count+=1
print(count)
