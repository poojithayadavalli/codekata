def small(l,n):
    l1=list(l)
    l2=[]
    for i in range(len(l1)):
        if(int(l1[i])<n):
            l2.append(l1[i])
    return ' '.join(l2)
n=int(input())
s=input().split()
print(small(s,n))
