m=int(input())
x=list(map(int,input().split()))
n=int(input())
y=list(map(int,input().split()))
for i in y:
    if i in x:
        flag=True
        pass
    else:
        flag=False
        break
if flag:
    print("Yes")
else:
    print("No")

