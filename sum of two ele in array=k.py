x=input().split()
k=int(x[1])
flag=False
y=list(map(int,input().split()))
m=[]
for i in range(len(y)-1):
    for j in range(i+1,len(y)):
        if y[i]+y[j]==k:
            print("yes")
            flag=True
            break
        else:
            pass
if flag==False:
    print("no")
    
