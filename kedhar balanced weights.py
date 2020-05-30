x=input().split('|')
y=input()
sum1=0
sum2=0
for i in x[0]:
    sum1+=ord(i)
for i in x[1]:
    sum2+=ord(i)
if sum1+ord(y)==ord(x[1]):
    x[0]=x[0]+y
else:
    x[1]=x[1]+y
print('|'.join(x))
#incomplete
