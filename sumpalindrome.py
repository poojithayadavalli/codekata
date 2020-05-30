n=input()
sum1=0
for i in n:
    sum1+=int(i)
x=str(sum1)
l=x[::-1]
print("yes" if x==l else "no")		
