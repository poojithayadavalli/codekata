def find(x,k):
    x1=dict(x)
    l=[]
    for x,h in x1.items():
        if(h==k):
            l.append(x)
    return l
n=input().split()
s=input().split()
res={}
def countFrequency(s): 
    freq={} 
    for item in s: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] =1
    return freq
res=countFrequency(s)
l=find(res,int(n[1]))
l.sort()
if(len(l)):
    print(' '.join(l))
else:
    print("-1")
