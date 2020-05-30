x=int(input())
x=list(bin(x)[2:])
#print(x)
for i in range(len(x)):
    if x[i]=='0':
        x[i]='1'
    elif x[i]=='1':
        x[i]='0'
y=[str(i) for i in x]
#print(y)
print(int(''.join(y),2))
