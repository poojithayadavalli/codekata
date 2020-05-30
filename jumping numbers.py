x=int(input())
if len(str(x))==1:
    print(x+1)
elif x==0:
    print("1")
else:
    count=10
    for i in range(10,x+1):
        h=str(i)
        for j in range(len(h)-1):
            if abs(int(h[j])-int(h[j+1]))!=1:
                flag=False
                break
            else:
                flag=True
        if flag:
            count+=1
    print(count)
                
        
        
