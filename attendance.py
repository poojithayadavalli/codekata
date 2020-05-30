n=int(input())
s=input().split()
acount=0
pcount=0
for i in range(n):
    if s[i]=="A":
        acount=acount+1
    elif s[i]=="P":
        pcount=pcount+1
if((pcount/n)>0.25):
    print("Not Blacklisted")
else:
    print("Blacklisted")
