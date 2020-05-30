from itertools import combinations 
s=str(input()) 
s=list(s) 
l=[] 
r=[]
for i in range(1,len(s)+1):
    m=list(combinations(s,i)) 
    for j in range(len(m)):
        temp1=list(m[j]) 
        temp1="".join(temp1)
        temp2=list(m[j])
        temp2.reverse() 
        temp2="".join(temp2) 
        if(temp1!=temp2):
            l.append(temp1)
            r.append(len(temp1)) 
print(l[r.index(max(r))])
