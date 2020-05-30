def find(x):
    x1=dict(x)
    for x,h in x1.items():
        if(h==2):
            return x
n=int(input())
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
print(find(res))
