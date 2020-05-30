n=int(input())
s=list(map(int,input().split()))
l=list(map(int,input().split()))
for i in range(n):
    x=s
    y=l
    x[i],y[i]=y[i],x[i]
    if(sum(x)==sum(y)):
        #print("Yes")
        flag=True
        break
    else:
        flag=False
print("No" if flag==False else "Yes")
#incomplete
