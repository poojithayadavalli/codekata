x=list(input())
#print(x)
l=[]
tmpone=0
ones=0
for i in range(len(x)):
    if x[i]=='1':
        tmpone+=1
        if tmpone>ones:
            ones=tmpone
            
    else:
        l.append(ones)
        tmpone=0
        ones=0
l.append(ones)
print(max(l))
