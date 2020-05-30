x,k=map(int,input().split())
l=[]
for i in range(x):
    l.append(input())
m=[]
flag=False
for i in range(x-k+1):
    m.append(l[i:k+i])
#print(m)
for i in m:
    h=i[0]
    for j in range(1,k):
        if i[j]!=h:
            break
        else:
            flag=True
    if flag:
        print("yes")
        break
if flag==False:
    print("no")
  
