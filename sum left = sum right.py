x=int(input())
s=list(map(int,input().split()))
flag=0
for i in range(2,len(s)-2):
    s1=list(map(int,s[:i]))
    s2=list(map(int,s[i+1:]))
    if sum(s1)==sum(s2):
        flag=True
        break
if(flag):
    print("yes")
else:
    print("no")
