y=list(input())
l=[]
flag=False
x=y
for i in range(len(y)):
    l.append(x[:i]+x[i+1:])
#print(l)
for i in l:
    if i[:len(i)//2]==i[len(i)//2:]:
        print("YES")
        flag=True
        break
if not flag:
    print("NO")
