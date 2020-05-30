n=input()
sum1=0
for i in n:
    if(i in ['a','e','i','o','u']):
        sum1+=ord(i)
print(sum1)
print("0" if sum1%8!=0 or sum1==0 else "1")
