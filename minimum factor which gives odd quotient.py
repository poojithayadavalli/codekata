n=int(input())
l=[]
if n>1:
    for i in range(1,n+1):
        if n%i==0 and (n//i)%2!=0:
            l.append(i)
    print(min(l))
else:
    print("1" if n==1 else "0")
