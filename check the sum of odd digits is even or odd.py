x=input()
sum1=0
for i in x:
    if int(i)%2!=0:
    	sum1+=int(i)
if sum1%2==0:
    print("E")
else:
    print("O")
