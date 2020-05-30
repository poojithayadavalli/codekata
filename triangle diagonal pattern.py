y=int(input())
l=[]
x=2*y
for i in range(y):
    l=""
    for j in range(x):
        if i==y-1:
            if j%2==0:
                l+=" "
            else:
                l+="*"
        else:
            if j==(x//2)-i or j==(x//2)+i:
                l+="*"
            else:
                l+=" "
    print(l)
