s=list(input())
res={}
freq={}
flag=1
for item in s: 
    if item in freq: 
        freq[item] += 1
        flag=0
    else:
        freq[item] =1
if flag==0:
    print("yes")
else:
    print("no")
