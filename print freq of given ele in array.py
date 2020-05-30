n,k=map(str,input().split())
s=input().split()
freq={}
for item in s: 
    if item in freq: 
        freq[item] += 1
    else:
        freq[item] =1
if k in freq:
    print("yes",end=" ")
    print(freq[k])
else:
    print("no")
    
