x=int(input())
y=input().split()
count=0
for i in range(1,x-1):
    if((y[i]<y[i+1] and y[i]<y[i-1])or(y[i]>y[i+1] and y[i]>y[i-1])):
    	count+=1
print(count)
