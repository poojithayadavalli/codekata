x=int(input())
s=list(map(int,input().split()))
flag=0
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        for k in range(j+1,len(s)):
            if(s[i]+s[j])==s[k]:
                flag=1
                print("yes")
                break
