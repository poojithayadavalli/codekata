x=input().split()
s=list(map(int,input().split()))
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]*s[j]==int(x[1]):
            print(i+1,j+1,sep=" ")
