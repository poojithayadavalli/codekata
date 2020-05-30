x=int(input())
y=[int(z) for z in input().split()]
sum1=sum(y)
if sum1%2==0 and sum1%3==0 and sum1%5==0:
    print("1")
else:
    print("0")
