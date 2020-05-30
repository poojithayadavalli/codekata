import operator
s=list(input())
freq={}
for item in s: 
    if item in freq: 
        freq[item] += 1
    else:
        freq[item] =1
f=sorted(freq.items(),key=operator.itemgetter(1),reverse=True)
l=[]
for i,k in f:
    l.append(i*k)
print(''.join(l))
