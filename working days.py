def prime(x):
    lst=[]
    for i in range(2,x+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
    print(lst)
    return(len(lst))
n=input().split()
y=int(n[1])
x=n[0]
if x=="january" or x=="march" or x=="may" or x=="july"or x=="august" or x=="october" or x=="december":
    z=prime(31)
elif x=="febraury":
    if y%400==0 and((y%100==0and y%400==0)or y%100!=0):
        z=prime(29)
    else:
        z=prime(28)
elif x=="april" or x=="june" or x=="september" or x=="november":
    z=(prime(30))
print(z)
