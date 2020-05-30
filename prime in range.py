l,r=map(int,input().split())
lst=[]
for i in range(l,r+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
print(len(lst))
