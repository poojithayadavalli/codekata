def getm(d,p):
    l=[]
    for i,j in d.items():
        if j<p:
            l.append(i)
    l.sort()
    return ' '.join(l)
n,k=map(int,input().split())
s=input().split()
freq={}
for item in s: 
    if item in freq: 
        freq[item] += 1
    else:
        freq[item] =1
print(getm(freq,k))
