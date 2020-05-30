n=list(input())
freq={} 
for item in n: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] =1
k=list(freq.items())
y=k[0][1]
for i,j in freq.items():
    if j==y:
        flag=True
    else:
        flag=False
        break
print("1" if flag else "0")

