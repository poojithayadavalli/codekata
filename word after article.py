h=['the','a','an','A','An','The']
x=input().split()
y=[]
for i in range(len(x)):
    if x[i] in h:
        if (i+1)<len(x) and x[i]=='The':
            y.append(x[i+1].capitalize())
        elif (i+1)<len(x):
            y.append(x[i+1])
print(' '.join(y))
