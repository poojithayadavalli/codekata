x=list(input())
l=[]
for i in x:
    if i in l:
        pass
    else:
        l.append(i)
print(''.join(l))
