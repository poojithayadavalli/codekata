x=list(input())
c=int(input())
m=int(input())
for i in range(len(x)):
    if i%m==0:
        if c==1:
            x[i-1]=x[i-1].lower()
        else:
            x[i-1]=x[i-1].upper()
print(' '.join(x))
