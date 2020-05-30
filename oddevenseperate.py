s=input()
e=[]
o=[]
for i in range(len(s)):
    if i%2==0:
    	e.append(s[i])
    else:
    	o.append(s[i])
print(''.join(e),end=" ")
print(''.join(o))
