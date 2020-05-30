s=list(input())
freq={}
for item in s: 
    if item in freq: 
        freq[item] += 1
    else:
        freq[item] =1
l=list()
for i in freq.keys():
    l.append(i)
for j,k in freq.items():
    if k>1:
        l.remove(j)
print(''.join(l))
#one test case
