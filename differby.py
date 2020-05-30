s=input().split()
x=int(s[2])
count=0
for i in range(len(s[0])):
    if(s[0][i]!=s[1][i]):
    	count+=1
if(count==x):
    print("yes")
else:
    print("no")
