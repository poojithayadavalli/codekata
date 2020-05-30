x=int(input())
flag=True
for j in range(2,x//2):
    if x==2:
        flag=True
        break
    elif x%j==0:
        flag=False
        break
    else:
        flag==True
print("yes" if flag else "no")

            
