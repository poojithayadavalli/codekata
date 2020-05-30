x=input()
x=bin(x)
print(x)
for i in range(0,len(x)-1,2):
    x[i],x[i+1]=x[i+1],x[i]
#for i in range(len(x)):
 #   if x[i]=='0':
 #       x[i]='1'
  #  elif x[i]=='1':
        #x[i]='0'
y=[str(i) for i in x]
print(y)
print(int(''.join(y),2))
#incomplete
