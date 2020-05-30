x=input().split()
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
try:
    if freq[x[1]]>1:
        print(freq[x[1]])
    else:
    	print("0")
except:
    print("-1")
