def getm(d):
    l=[]
    v=list(d.values())
    k=list(d.keys())
    for i,j in d.items():
        if j==min(v):
            l.append(i)
    return ''.join(l)
s=input().split()
s=''.join(s)
freq={}
for item in s: 
    if item in freq: 
        freq[item] += 1
    else:
        freq[item] =1
print(getm(freq))
