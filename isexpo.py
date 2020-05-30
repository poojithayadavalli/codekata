s=input().split()
flag=1
for i in range(1,int(s[0])):
    if(int(s[1])**i==int(s[0])):
    	flag=0
if(flag==0):
    print("yes")
else:
    print("no")
