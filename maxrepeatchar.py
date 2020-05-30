def getm(d):
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
x=int(input())
s=input().split()
freq={}
for item in s: 
    if item in freq: 
        freq[item] += 1
    else:
        freq[item] =1
print(getm(freq))
