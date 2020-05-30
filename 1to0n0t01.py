n=input()
count=0
l=[]
for i in range(len(n)):
    if n[i]=='0':
        l.append(str(i))
        count+=1
    if count==2:
        break
print(' '.join(l))
