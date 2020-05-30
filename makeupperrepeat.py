s=input()
s1=s.replace(' ','-')
x=list(s1)
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            x[i]=x[i].upper()
            x[j]=x[j].upper()
y=''.join(x)
y1=y.replace('-',' ')
print(y1)
#incomplete
    	
