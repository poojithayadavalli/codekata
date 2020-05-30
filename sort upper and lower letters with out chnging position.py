l=str(input())
l=list(l) 
t1=[]
t2=[]
for i in range(len(l)):
    if(l[i].isupper()):
        t1.append(l[i])
    else:
        t2.append(l[i])
t1.sort()
t2.sort()
for i in range(len(l)):
    if(l[i].isupper()):
        l[i]=t1[0] 
        t1.pop(0)
    else:
        l[i]=t2[0]
        t2.pop(0) 
print("".join(l))
